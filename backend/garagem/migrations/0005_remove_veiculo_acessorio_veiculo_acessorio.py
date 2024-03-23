# Generated by Django 5.0.3 on 2024-03-23 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0004_alter_acessorio_options_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='acessorio',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='acessorio',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.acessorio'),
            preserve_default=False,
        ),
    ]
