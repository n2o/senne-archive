from django.shortcuts import render

from archive.models import Item
from frontpage.models import Frontpage


def index(request):
    public = Item.objects.filter(public=True)
    decades = public.decades()
    return render(
        request,
        "frontpage/index.html",
        {
            "frontpage": Frontpage.objects.first(),
            "decades": decades,
            "total": sum(n for _, _, n in decades),
            "recent": public.order_by("-created")[:4],
        },
    )
