from django.utils import timezone


class LogIPWriterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        now = timezone.now()

        ip = request.META.get('REMOTE_ADDR', 'ip addres nomalum')

        # print(f'{[now]} ip address {ip}')

        return self.get_response(request)


class LogUserAgentWriterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        now = timezone.now()

        user_agent = request.headers.get('User-Agent')

        # print(f'{[now]} ip address {user_agent}')
        return self.get_response(request)
