# Generated by Django 4.2.4 on 2023-10-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_alter_reserva_data_alter_reserva_observacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='lido',
            field=models.BooleanField(blank=True, default=False, verbose_name='Lido'),
        ),
    ]