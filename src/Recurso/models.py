from django.db import models

# Create your models here.
from Evento.models import Logistica, Evento
from Neglected.models import Timedate
from Utilizadores.models import Servicostecnicos
from django.core.validators import RegexValidator


class Unidadeorganica(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    universidadeid = models.ForeignKey('Universidade', models.DO_NOTHING,
                                       db_column='UniversidadeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnidadeOrganica'
        unique_together = ('Nome', 'universidadeid')


class Universidade(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255, unique=True)  # Field name made lowercase.
    localizacao = models.CharField(db_column='Localizacao', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Universidade'


class Empresa(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255, unique=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', max_length=255)  # Field name made lowercase.
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    telefone = models.CharField(db_column='Telefone', validators=[phone_regex], max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=255)  # Field name made lowercase.
    endereco_regex = RegexValidator(regex=r"^(?=[^A-Za-z]*[A-Za-z])[ -~]*$")
    endereco = models.CharField(db_column='Endereço', validators=[endereco_regex],
                                max_length=255)  # Field name made lowercase.
    codigopostal_regex = RegexValidator(regex=r'^\d{4}-\d{3}?$')
    codigopostal = models.CharField(db_column='CodigoPostal', validators=[codigopostal_regex],
                                    max_length=255)  # Field name made lowercase.
    faturacao_regex = RegexValidator(regex=r'^\d*$')
    faturacao = models.CharField(db_column='Faturacao', validators=[faturacao_regex], max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresa'


class Servico(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255, unique=True)  # Field name made lowercase.
    Descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)
    unidadeorganicaid = models.ForeignKey('Unidadeorganica', models.DO_NOTHING, db_column='UnidadeOrganicaID',
                                          blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Servico'


class EventoRecurso(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    recursoid = models.ForeignKey('Recurso', models.DO_NOTHING, db_column='RecursoID')  # Field name made lowercase.
    timedateid = models.ForeignKey('TimedateRecurso', models.DO_NOTHING, db_column='TimeDate')  # Field name made 

    class Meta:
        managed = False
        unique_together = ('eventoid', 'recursoid')
        db_table = 'Evento_Recurso'


class Campus(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    universidadeid = models.ForeignKey('Universidade', models.DO_NOTHING,
                                       db_column='UniversidadeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Campus'
        unique_together = ('Nome', 'universidadeid')


class Edificio(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    localizacao = models.CharField(db_column='Localizaçao', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.DO_NOTHING, db_column='CampusID', blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Edificio'
        unique_together = ('Nome', 'campusid')


class Espaco(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255)
    tipo = models.CharField(db_column='Tipo', max_length=255)
    capacidade = models.IntegerField(db_column='Capacidade')  # Field name made lowercase.
    mobilidade = models.BooleanField(db_column='Mobilidade')  # Field name made lowercase.
    edificioid = models.ForeignKey('Edificio', models.DO_NOTHING, db_column='EdificioID', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Espaco'
        unique_together = ('Nome', 'edificioid')


class Equipamento(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', unique=True, max_length=255)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, null=True,
                                 blank=True)  # Field name made lowercase.
    unidadeorganicaid = models.ForeignKey('Unidadeorganica', models.DO_NOTHING,
                                          db_column='UnidadeOrganicaID', blank=True,
                                          null=True)  # Field name made lowercase.
    espacoid = models.ForeignKey('Espaco', models.DO_NOTHING, db_column='Espacoid', blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Equipamento'


class Recurso(models.Model):
    def __str__(self):
        return self.Nome

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    fonte = models.CharField(db_column='Fonte', max_length=255)  # Field name made lowercase.
    empresaid = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='EmpresaID', blank=True,
                                  null=True)  # Field name made lowercase.
    espacoid = models.ForeignKey(Espaco, models.DO_NOTHING, db_column='EspacoId', blank=True, null=True)
    servicoid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='ServicoId', blank=True, null=True)
    equipamentoid = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='EquipamentoId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Recurso'


class Componente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    empresaid = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='EmpresaId', blank=True,
                                  null=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.DO_NOTHING, db_column='CampusId', blank=True,
                                 null=True)  # Field name made lowercase.
    edificioid = models.ForeignKey(Edificio, models.DO_NOTHING, db_column='EdificioId', blank=True,
                                   null=True)  # Field name made lowercase.
    unidade_organicaid = models.ForeignKey(Unidadeorganica, models.DO_NOTHING, db_column='UOrganicaId', blank=True,
                                           null=True)  # Field name made lowercase.
    universidadeid = models.ForeignKey(Universidade, models.DO_NOTHING, db_column='UniversidadeId', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecursoComponente'


class Tipoespaco(models.Model):
    def __str__(self):
        return self.nome

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)
    logisticaid = models.ForeignKey(Logistica, models.DO_NOTHING, db_column='Logisticaid')  # Field name made lowercase.
    horariorequisicao = models.ForeignKey(Timedate, models.DO_NOTHING,
                                          db_column='HorarioRequisicao')  # Field name made lowercase.
    isAttributed = models.IntegerField(db_column='IsAttributed', null=True)

    class Meta:
        managed = False
        db_table = 'TipoEspaco'


class Tiposervico(models.Model):
    def __str__(self):
        return self.nome

    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)
    logisticaid = models.ForeignKey(Logistica, models.DO_NOTHING, db_column='Logisticaid')  # Field name made lowercase.
    horariorequisicao = models.ForeignKey(Timedate, models.DO_NOTHING,
                                          db_column='HorarioRequisicao')  # Field name made lowercase.
    isAttributed = models.IntegerField(db_column='IsAttributed', null=True)

    class Meta:
        managed = False
        db_table = 'TipoServico'


class Tipodeequipamento(models.Model):
    def __str__(self):
        return self.nome


    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)
    logisticaid = models.ForeignKey(Logistica, models.DO_NOTHING, db_column='Logisticaid')  # Field name made lowercase.
    horariorequisicao = models.ForeignKey(Timedate, models.DO_NOTHING,
                                          db_column='HorarioRequisicao')  # Field name made lowercase.
    isAttributed = models.IntegerField(db_column='IsAttributed', null=True)

    class Meta:

        managed = False
        db_table = 'TipodeEquipamento'


class TimedateRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    timedateid = models.ForeignKey(Timedate, models.DO_NOTHING, db_column='TimeDateID')  # Field name made lowercase.
    recursoid = models.ForeignKey(Recurso, models.DO_NOTHING, db_column='RecursoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeDate_Recurso'
        unique_together = (('timedateid', 'recursoid'),)
