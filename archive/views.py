from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Author, Item

PAGE_SIZE = 20


def index(request):
    query = request.GET.get("q", "").strip()
    author = _author_from_param(request.GET.get("autor"))
    items = _query_items(query, author)
    page = Paginator(items, PAGE_SIZE).get_page(request.GET.get("seite"))
    return render(request, "archive/index.html", {
        "items": page,
        "authors": Author.objects.order_by("lastname", "firstname"),
        "query": query,
        "selected_author": author,
        "searched": bool(query or author),
        "empty_search": "q" in request.GET and not (query or author),
    })


def _author_from_param(value):
    if value and value.isascii() and value.isdigit():
        return Author.objects.filter(pk=value).first()
    return None


def _query_items(query, author):
    if not (query or author):
        return Item.objects.none()
    items = Item.objects.filter(public=True).select_related("author").order_by("title", "pk")
    if query:
        items = items.filter(
            Q(title__icontains=query) | Q(abstract__icontains=query)
            | Q(notes__icontains=query) | Q(keywords__icontains=query)
        )
    if author:
        items = items.filter(author=author)
    return items


def detail(request, pk):
    item = get_object_or_404(Item.objects.select_related("author"), pk=pk, public=True)
    return render(request, "archive/detail.html", {"item": item})


def media(request, name):
    """Old /media/... links (indexed by Google) → fresh signed S3 URL, for files of public items only."""
    fields = ("file1", "file2", "file3", "image1", "image2", "image3")
    match = Q()
    for field in fields:
        match |= Q(**{field: name})
    if not Item.objects.filter(match, public=True).exists():
        raise Http404
    return redirect(default_storage.url(name))
