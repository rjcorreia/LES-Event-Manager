# Generated by Django 3.2 on 2021-05-07 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestorTemplates', '0002_auto_20210422_2340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='campoformulario',
            options={},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={},
        ),
        migrations.AlterModelOptions(
            name='formulario',
            options={},
        ),
        migrations.AlterModelOptions(
            name='resposta',
            options={},
        ),
        migrations.AlterModelOptions(
            name='respostaspossiveis',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tipocampo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tipoformulario',
            options={},
        ),
        migrations.DeleteModel(
            name='GcpFormulario',
        ),
    ]