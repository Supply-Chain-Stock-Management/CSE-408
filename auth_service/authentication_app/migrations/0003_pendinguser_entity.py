# Generated by Django 5.0.2 on 2024-03-02 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0002_entity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendinguser',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pending_users', to='authentication_app.entity'),
        ),
    ]