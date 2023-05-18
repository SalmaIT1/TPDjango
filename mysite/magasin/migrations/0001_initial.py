# Generated by Django 4.1.7 on 2023-02-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('type', models.CharField(choices=[('fr', 'Frais'), ('cs', 'Conserve'), ('em', 'emballé')], default='em', max_length=2)),
            ],
        ),
    ]
