import base64
import os

from django.conf import settings


def secure_compare(a, b):
    """Comparazione in tempo costante per evitare timing attacks.

    Python 2.7.7 ha `hmac.compare_digest` ma non possiamo usarlo ancora :(
    """
    return sum(1 for i, j in zip(a, b) if i != j) == 0


def generate_token():
    return base64.b64encode(os.urandom(20))

