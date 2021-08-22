# Generated by Django 3.2.6 on 2021-08-22 19:58

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0010_empresa_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresa.empresa'),
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='despesas',
        ),
        migrations.AddField(
            model_name='empresa',
            name='despesas',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=12),
        ),
    ]
