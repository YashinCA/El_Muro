# Generated by Django 4.0.2 on 2022-03-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
