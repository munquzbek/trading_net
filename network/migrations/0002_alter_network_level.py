# Generated by Django 5.0.7 on 2024-07-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Hierarchy Level'),
        ),
    ]
