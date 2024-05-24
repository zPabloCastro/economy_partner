# Generated by Django 5.0.6 on 2024-05-23 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('economy_partner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='initial_balance',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='economy_partner.account'),
        ),
    ]
