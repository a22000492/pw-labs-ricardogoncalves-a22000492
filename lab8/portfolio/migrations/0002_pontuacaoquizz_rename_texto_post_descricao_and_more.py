# Generated by Django 4.0.4 on 2022-05-11 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pontuacao', models.IntegerField(validators=[django.core.validators.MinValueValidator(2)])),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='texto',
            new_name='descricao',
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.CharField(default='Ricardo Gonçalves', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]