from manifesti.token import secure_compare
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
    if request.method == "POST":
        token = request.POST.get("token")
        id = request.POST.get("id")
        if token and id:
            posizione = Posizione.objects.get(pk=id)
            if posizione:
               if secure_compare(posizione.token, token):
                    posizione.ultima_visita = timezone.now()
                    posizione.fatto = True
                    posizione.save()
                    info(request, "Grazie del tuo aiuto!")
               else:
                    info(request, "Token non valido :(")
            else:
                return HttpResponse("Dai gattuso, basta...", content_type="text/plain", status=401)
        else:
            info(request, "Mancano dei pezzi...")

    return render(request, "main.html",  {"posizioni": Posizione.objects.all()})
