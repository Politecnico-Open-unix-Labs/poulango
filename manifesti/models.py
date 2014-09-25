from django.db import models

class Posizione(models.Model):
    descrizione = models.TextField()
    latitudine = models.DecimalField(max_digits=18, decimal_places=14)
    longitudine = models.DecimalField(max_digits=18, decimal_places=14)
    ultima_visita = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        db_table = u'Posizioni'
        verbose_name_plural = u'Posizioni'

    def __str__(self):
        return self.descrizione
