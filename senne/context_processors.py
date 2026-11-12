from archive.models import Author


def search(request):
    """The search form sits in the header of every page."""
    return {"authors": Author.objects.order_by("lastname", "firstname").only("pk", "lastname", "firstname", "title")}
