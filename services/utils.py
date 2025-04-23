from django.core.exceptions import PermissionDenied


def superadmin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapper


def superadmin_blocked(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapper


def barber_required(view_func):
    pass


def barber_blocked(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name="barber").exists():
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapper


def client_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_superuser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return wrapper
