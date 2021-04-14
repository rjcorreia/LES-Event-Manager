from django.db import models

# Create your models here.
from Evento.models import Evento
from Utilizadores.models import User


class Inscricao(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    telemovel = models.IntegerField(db_column='Telemovel', blank=True, null=True)  # Field name made lowercase.
    idade = models.IntegerField(db_column='Idade')  # Field name made lowercase.
    profissao = models.CharField(db_column='Profissao', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inscricao'

