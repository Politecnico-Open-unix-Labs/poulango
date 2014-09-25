from django.contrib import admin
from manifesti.models import Posizione


def reset_fatto(modeladmin, request, queryset):
    queryset.update(fatto=False)

reset_fatto.short_description = "Riporta bacheca a 'non fatto'"

class PosizioneAdmin(admin.ModelAdmin):
    list_display = ("descrizione", "fatto", "token", "latitudine", "longitudine", "ultima_visita")
    actions = (reset_fatto, )

admin.site.register(Posizione, PosizioneAdmin)
