# Generated by Django 3.2 on 2021-04-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informacaomensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('pendente', models.IntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('lido', models.IntegerField()),
                ('emissorid', models.IntegerField(blank=True, null=True)),
                ('recetorid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'informacaomensagem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mensagemenviada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem_id', models.IntegerField()),
            ],
            options={
                'db_table': 'mensagemenviada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mensagemrecebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem_id', models.IntegerField()),
            ],
            options={
                'db_table': 'mensagemrecebida',
                'managed': False,
            },
        ),
    ]
