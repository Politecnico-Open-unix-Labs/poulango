from django.contrib import admin

from manifesti.models import Posizione
from manifesti.token import generate_token


def reset_fatto(modeladmin, request, queryset):
    queryset.update(fatto=False)

reset_fatto.short_description = "Segna come 'non fatto'"


def set_fatto(modeladmin, request, queryset):
    queryset.update(fatto=True)

set_fatto.short_description = "Segna come 'fatto'"


def reset_token(modeladmin, request, queryset):
    for posizione in queryset:
        posizione.update_token()
        posizione.save()

reset_token.short_description = "Genera nuovo token"


class PosizioneAdmin(admin.ModelAdmin):
    list_display = ("descrizione", "fatto", "token", "ultima_visita")
    actions = (set_fatto, reset_fatto, reset_token)

admin.site.register(Posizione, PosizioneAdmin)
