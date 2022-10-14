# Generated by Django 4.0.3 on 2022-10-13 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bancos',
            old_name='nombre',
            new_name='nombreB',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='nombre',
            new_name='nombreC',
        ),
        migrations.RenameField(
            model_name='pagos',
            old_name='banco',
            new_name='deuda',
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='cliente',
        ),
    ]
