# Generated by Django 5.1.1 on 2024-10-09 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lab', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtest',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_tests', to='patients.patient'),
        ),
    ]
