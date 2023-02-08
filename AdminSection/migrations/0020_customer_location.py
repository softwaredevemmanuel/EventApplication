# Generated by Django 4.1.3 on 2023-01-12 13:17

import AdminSection.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0019_customer_event_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="location",
            field=models.CharField(
                default=None, max_length=100, verbose_name=AdminSection.models.Event
            ),
        ),
    ]