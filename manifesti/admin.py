from django.contrib import admin
from manifesti.models import Posizione


class PosizioneAdmin(admin.ModelAdmin):
    list_display = ("descrizione", "latitudine", "longitudine", "ultima_visita")

admin.site.register(Posizione, PosizioneAdmin)

