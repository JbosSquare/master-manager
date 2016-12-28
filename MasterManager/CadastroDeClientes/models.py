from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    created_date = models.DateTimeField(default=timezone.now)
    creator_user = models.ForeignKey('auth.User')

    def create(self):
        self.save()

    def __str__(self):
        return self.nome + ' - ' + self.cpf
