# Generated by Django 3.2.6 on 2021-08-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0014_funcionario_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='link',
            field=models.SlugField(blank=True, default='/', max_length=120, unique=True),
        ),
    ]
