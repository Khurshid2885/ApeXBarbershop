from random import randint

from django.core.exceptions import PermissionDenied

from accounts.models import Code


def generate_code(user):
    code = randint(1000, 9999)

    Code.objects.create(code=code, user=user)

    return code


def is_not_authenticated(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            raise PermissionDenied("You can not access this page as you have already registered!")
        return func(request, *args, **kwargs)

    return wrapper
