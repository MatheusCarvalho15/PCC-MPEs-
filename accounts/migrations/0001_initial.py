# Generated by Django 4.2.8 on 2024-07-08 23:20

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('cargo', models.CharField(blank=True, choices=[('vendedor', 'Vendedor'), ('caixa', 'Caixa'), ('funcionario', 'Funcionario')], max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
