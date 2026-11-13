from django.http import Http404
from django.test import TestCase

from archive.models import Author, Item, replace_umlauts
from senne.templatetags.senne_common import file_kind, markdown


class ReplaceUmlautsTest(TestCase):
    def test_umlauts_should_be_replaced(self):
        self.assertEqual("ae", replace_umlauts("ä"))
        self.assertEqual("aeoeue", replace_umlauts("äöü"))
        self.assertEqual("ssome Uemlauts", replace_umlauts("ßome Ümlauts"))


class ArchiveViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(lastname="Lakmann", firstname="Gerd")
        cls.public = Item.objects.create(title="Senne Heide", medart="Buch", author=author)
        cls.hidden = Item.objects.create(title="Senne intern", medart="Buch", author=author, public=False)

    def get(self, url):
        return self.client.get(url, secure=True)

    def test_search_lists_only_public_items(self):
        response = self.get("/archiv/?q=senne")
        self.assertContains(response, "Senne Heide")
        self.assertNotContains(response, "Senne intern")

    def test_archive_can_be_browsed_and_filtered(self):
        Item.objects.create(title="Dünen", medart="Foto(s)", year=1958, author=self.public.author)
        Item.objects.filter(pk=self.public.pk).update(year=1980)
        response = self.get("/archiv/")
        self.assertContains(response, "Senne Heide")
        self.assertContains(response, "Dünen")
        self.assertContains(response, "2 Belege")
        response = self.get("/archiv/?jahrzehnt=1950")
        self.assertContains(response, "Dünen")
        self.assertNotContains(response, "Senne Heide")
        response = self.get("/archiv/?art=Buch")
        self.assertContains(response, "Senne Heide")
        self.assertNotContains(response, "Dünen")
        # With a media type chosen, the decade counts only count that media type.
        response = self.get("/archiv/?art=Buch")
        self.assertEqual(response.context["decades"], [("1980", "1980er", 1)])
        # Unknown facet values are ignored instead of filtering everything away.
        self.assertContains(self.get("/archiv/?jahrzehnt=1&art=Unsinn"), "2 Belege")

    def test_typo_years_count_as_undated(self):
        Item.objects.filter(pk=self.public.pk).update(year=1980)
        for year in (-11975, 5, 11985, None):
            Item.objects.create(title=f"Tippfehler {year}", medart="Buch", year=year)
        response = self.get("/archiv/")
        self.assertEqual(response.context["decades"], [("1980", "1980er", 1), ("ohne", "ohne Jahr", 4)])
        undated = self.get("/archiv/?jahrzehnt=ohne")
        self.assertContains(undated, "4 Belege")
        self.assertNotContains(undated, "anno 11985")
        # A typo just past the range belongs to "ohne Jahr" only, never to the 2100 decade.
        Item.objects.create(title="Tippfehler 2105", medart="Buch", year=2105)
        self.assertFalse(Item.objects.in_decade("2100").exists())
        # Typos sort after the dated items instead of first.
        self.assertEqual(list(response.context["items"])[0], self.public)

    def test_detail_links_back_to_the_results_it_came_from(self):
        url = f"/archiv/{self.public.pk}"
        response = self.client.get(url, secure=True, HTTP_REFERER="https://testserver/archiv/?q=heide")
        self.assertContains(response, 'href="/archiv/?q=heide"')
        response = self.client.get(url, secure=True, HTTP_REFERER="https://evil.example/archiv/?q=x")
        self.assertContains(response, 'href="/archiv/">Zum Archiv')

    def test_hidden_item_detail_is_404(self):
        self.assertEqual(self.get(f"/archiv/{self.hidden.pk}").status_code, 404)
        self.assertEqual(self.get(f"/archiv/{self.public.pk}").status_code, 200)

    def test_old_media_links_redirect_only_for_public_items(self):
        from django.test import RequestFactory

        from archive.views import media

        Item.objects.filter(pk=self.public.pk).update(file1="archive/x/public.pdf")
        Item.objects.filter(pk=self.hidden.pk).update(file1="archive/x/hidden.pdf")
        request = RequestFactory().get("/")
        self.assertEqual(media(request, "archive/x/public.pdf").status_code, 302)
        for name in ("archive/x/hidden.pdf", "archive/x/unknown.pdf"):
            with self.assertRaises(Http404):
                media(request, name)

    def test_garbage_params_do_not_crash(self):
        for query in ("?q=senne&seite=abc", "?q=senne&seite=999", "?autor=xyz", "?autor=99999", "?autor=%C2%B2", "?q="):
            self.assertEqual(self.get(f"/archiv/{query}").status_code, 200, query)

    def test_field_values_are_escaped(self):
        Item.objects.filter(pk=self.public.pk).update(abstract="<script>x</script>")
        response = self.get(f"/archiv/{self.public.pk}")
        self.assertNotContains(response, "<script>x")
        self.assertContains(response, "&lt;script&gt;x")

    def test_file_kind(self):
        self.assertEqual(file_kind("archive/a/Bericht.pdf"), "PDF")
        self.assertEqual(file_kind("archive/a/ohne-endung"), "Datei")

    def test_markdown_is_sanitized(self):
        html = markdown('## Hi\n\n<script>alert(1)</script>[x](javascript:alert(1)){: onclick="alert(1)"}')
        self.assertIn("<h2>Hi</h2>", html)
        for bad in ("<script", "javascript:", "onclick"):
            self.assertNotIn(bad, html)


class FlatpageTest(TestCase):
    def test_impressum_renders_markdown(self):
        from django.contrib.flatpages.models import FlatPage

        page = FlatPage.objects.create(url="/impressum/", title="Impressum", content="## Angaben")
        page.sites.add(1)
        response = self.client.get("/impressum/", secure=True)
        self.assertContains(response, "<h2>Angaben</h2>", html=True)
        self.assertEqual(self.client.get("/impressum", secure=True).status_code, 301)

    def test_missing_slash_redirects_and_unknown_is_404(self):
        self.assertRedirects(self.client.get("/archiv", secure=True), "/archiv/", 301, fetch_redirect_response=False)
        self.assertEqual(self.client.get("/gibt-es-nicht/", secure=True).status_code, 404)
