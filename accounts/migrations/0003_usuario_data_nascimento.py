# Generated by Django 4.2.8 on 2024-05-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_usuario_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]