from django.contrib import admin

from manifesti.models import Posizione
from manifesti.token import generate_token


def reset_fatto(modeladmin, request, queryset):
    queryset.update(fatto=False)

reset_fatto.short_description = "Riporta bacheca a 'non fatto'"


def reset_token(modeladmin, request, queryset):
    for posizione in queryset:
        posizione.update_token()
        posizione.save()

reset_token.short_description = "Genera nuovo token"


class PosizioneAdmin(admin.ModelAdmin):
    list_display = ("descrizione", "fatto", "token", "ultima_visita")
    actions = (reset_fatto, reset_token)

admin.site.register(Posizione, PosizioneAdmin)
