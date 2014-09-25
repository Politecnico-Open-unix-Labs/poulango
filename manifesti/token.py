import hmac
import hashlib
import base64

from django.conf import settings


def secure_compare(a, b):
    """Comparazione in tempo costante per evitare timing attacks.

    Python 2.7.7 ha `hmac.compare_digest` ma non possiamo usarlo ancora:(
    """
    return sum(1 for i, j in zip(a, b) if i != j) == 0


def calculate_token(id):
    return base64.b64encode(hmac.new(settings.HMAC_KEY, unicode(id), hashlib.sha1).digest())
