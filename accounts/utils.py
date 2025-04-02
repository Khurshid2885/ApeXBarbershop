from random import randint
from accounts.models import Code


def generate_code(user):
    code = randint(1000, 9999)

    Code.objects.create(code=code, user=user)

    return code
