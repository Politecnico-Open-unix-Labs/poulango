from manifesti.token import less_shitty_compare, calculate_token
from models import Posizione

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages


def info(request, text):
    """Aggiungi un messaggio per l'utente in coda."""
    return messages.add_message(request, messages.INFO, text)


def main(request):
    """Handler della pagina"""
    def valid(id, token):
        return less_shitty_compare(calculate_token(id), token)

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
