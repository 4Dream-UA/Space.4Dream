from .models import ActionLog


class ActionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            path = request.path

            if (
                not path.startswith("/static/")
                and not path.startswith("/media/")
                and "/jsi18n/" not in path
            ):
                ActionLog.objects.create(
                    user=request.user,
                    method=request.method,
                    path=path,
                    status_code=response.status_code,
                )

        return response
