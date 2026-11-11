from django.test import TestCase

from archive.models import Author, Item, replace_umlauts
from senne.templatetags.senne_common import heading_if_field_exists, markdown


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

    def test_hidden_item_detail_is_404(self):
        self.assertEqual(self.get(f"/archiv/{self.hidden.pk}").status_code, 404)
        self.assertEqual(self.get(f"/archiv/{self.public.pk}").status_code, 200)

    def test_garbage_params_do_not_crash(self):
        for query in ("?q=senne&seite=abc", "?q=senne&seite=999", "?autor=xyz", "?autor=99999", "?autor=%C2%B2", "?q="):
            self.assertEqual(self.get(f"/archiv/{query}").status_code, 200, query)

    def test_field_values_are_escaped(self):
        self.assertNotIn("<script>", heading_if_field_exists("<script>x</script>", "Abstract"))

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
