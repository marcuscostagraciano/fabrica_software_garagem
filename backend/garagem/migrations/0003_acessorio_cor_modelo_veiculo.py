# Generated by Django 5.0.3 on 2024-03-23 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelo', to='garagem.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelo', to='garagem.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=0, null=True)),
                ('descricao', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('acessorio', models.ManyToManyField(related_name='veiculos', to='garagem.acessorio')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.cor')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.modelo')),
            ],
        ),
    ]
