from urllib.parse import urlsplit

from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

from .models import Author, Item, decade_label

PAGE_SIZE = 20


def index(request):
    query = request.GET.get("q", "").strip()
    author = _author_from_param(request.GET.get("autor"))
    items = _search(query, author)

    decades = items.decades()
    medarts = items.medarts()
    decade = _pick(request, "jahrzehnt", [value for value, _, _ in decades])
    medart = _pick(request, "art", [value for value, _ in medarts])
    # Each facet counts within the other facet's filter, so a count always matches the list it leads to.
    by_decade = items.in_decade(decade)
    by_medart = items.filter(medart=medart) if medart else items
    if medart:
        decades = by_medart.decades()
    if decade:
        medarts = by_decade.medarts()
    items = by_decade.filter(medart=medart) if medart else by_decade

    page = Paginator(items, PAGE_SIZE).get_page(request.GET.get("seite"))
    return render(
        request,
        "archive/index.html",
        {
            "items": page,
            "page_range": page.paginator.get_elided_page_range(page.number, on_each_side=1, on_ends=1),
            "query": query,
            "selected_author": author,
            "decades": decades,
            "medarts": medarts,
            "decade": decade,
            "decade_label": decade_label(decade) if decade else "",
            "medart": medart,
        },
    )


def _pick(request, param, allowed):
    """The parameter's value if it is one of the offered facet values, else ''."""
    value = request.GET.get(param, "")
    return value if value in allowed else ""


def _author_from_param(value):
    if value and value.isascii() and value.isdigit():
        return Author.objects.filter(pk=value).first()
    return None


def _search(query, author):
    items = Item.objects.filter(public=True).select_related("author").chronological()
    if query:
        items = items.filter(
            Q(title__icontains=query)
            | Q(abstract__icontains=query)
            | Q(notes__icontains=query)
            | Q(keywords__icontains=query)
        )
    if author:
        items = items.filter(author=author)
    return items


def detail(request, pk):
    item = get_object_or_404(Item.objects.select_related("author"), pk=pk, public=True)
    # Back to the result list the visitor came from, if any.
    referer = request.META.get("HTTP_REFERER", "")
    parts = urlsplit(referer)
    from_results = (
        parts.query
        and parts.path == reverse("archive:index")
        and url_has_allowed_host_and_scheme(referer, {request.get_host()})
    )
    back = f"{parts.path}?{parts.query}" if from_results else None
    return render(request, "archive/detail.html", {"item": item, "back": back})


def media(request, name):
    """Old /media/... links (indexed by Google) → fresh signed S3 URL, for files of public items only."""
    match = Q()
    for field in Item.FILE_FIELDS + Item.IMAGE_FIELDS:
        match |= Q(**{field: name})
    if not Item.objects.filter(match, public=True).exists():
        raise Http404
    return redirect(default_storage.url(name))
