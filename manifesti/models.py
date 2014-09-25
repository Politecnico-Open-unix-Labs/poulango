from django.db import models
from manifesti.token import generate_token


class Posizione(models.Model):
    descrizione = models.TextField()
    latitudine = models.DecimalField(max_digits=18, decimal_places=14)
    longitudine = models.DecimalField(max_digits=18, decimal_places=14)
    ultima_visita = models.DateTimeField(null=True, blank=True, editable=False)
    fatto = models.BooleanField(default=False)
    token = models.CharField(max_length=32, default=generate_token, editable=False)

    class Meta:
        db_table = u'Posizioni'
        verbose_name_plural = u'Posizioni'

    def __str__(self):
        return self.descrizione

    def update_token(self):
        self.token = generate_token()
