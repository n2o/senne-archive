from django.http import HttpResponse


def healthz(get_response):
    """Answer kubelet probes before host validation and the HTTPS redirect (probes use the pod IP, plain HTTP)."""

    def middleware(request):
        if request.path == "/healthz":
            return HttpResponse("ok", content_type="text/plain")
        return get_response(request)

    return middleware
