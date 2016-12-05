# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('finalizado', models.BooleanField(default=False)),
                ('iniciado', models.DateTimeField(default=django.utils.timezone.now)),
                ('jogadasMaxima', models.IntegerField(default=0)),
                ('jogadasJogador1', models.IntegerField(default=0)),
                ('jogadasJogador2', models.IntegerField(default=0)),
                ('jogador1', models.ForeignKey(related_name='jogador1', to=settings.AUTH_USER_MODEL)),
                ('jogador2', models.ForeignKey(related_name='jogador2', to=settings.AUTH_USER_MODEL)),
                ('vencendor', models.ForeignKey(null=True, related_name='vencedor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posicao',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('linha', models.IntegerField(default=0)),
                ('coluna', models.IntegerField(default=0)),
                ('barco', models.BooleanField(default=False)),
                ('verificado', models.BooleanField(default=False)),
                ('acerto', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tabuleiro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.IntegerField(default=0)),
                ('jogo', models.ForeignKey(related_name='jogo', to='jogo.Jogo')),
            ],
        ),
        migrations.AddField(
            model_name='posicao',
            name='tabuleiro',
            field=models.ForeignKey(default=0, related_name='tabuleiro', to='jogo.Tabuleiro'),
        ),
    ]
