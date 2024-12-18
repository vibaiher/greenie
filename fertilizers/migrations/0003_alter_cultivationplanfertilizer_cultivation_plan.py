# Generated by Django 5.1.2 on 2024-10-25 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fertilizers', '0002_cultivationplan_cultivationplanfertilizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivationplanfertilizer',
            name='cultivation_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fertilizers', to='fertilizers.cultivationplan'),
        ),
    ]
