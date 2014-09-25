import hmac
import hashlib
import base64

from models import Posizione

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages

def less_shitty_compare(a, b):
    """Comparazione in tempo costante per evitare timing attacks.

    Python 2.7.7 ha `hmac.compare_digest` ma non possiamo usarlo ancora:(
    """
    return sum(i == j for i, j in zip(a, b)) > 0


def info(request, text):
    """Aggiungi un messaggio per l'utente in coda."""
    return messages.add_message(request, messages.INFO, text)


def main(request):
    """Handler della pagina"""
    def valid(id, token):
        shouldbe = base64.b64encode(hmac.new(settings.HMAC_KEY, id, hashlib.sha1).digest())
        print shouldbe
        return less_shitty_compare(shouldbe, token)

    if request.method == "POST":
        token = request.POST.get("token")
        id = request.POST.get("id")
        if token and id:
            if valid(id, token):
                posizione = Posizione.objects.get(pk=id)
                if posizione:
                    posizione.ultima_visita = timezone.now()
                    posizione.save()
                    info(request, "Grazie del tuo aiuto!")
                else:
                    return HttpResponse("Dai gattuso, basta...", content_type="text/plain")
            else:
                info(request, "Token non valido :(")

    return render(request, "main.html",  {"posizioni": Posizione.objects.all()})
