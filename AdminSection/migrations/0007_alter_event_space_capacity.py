# Generated by Django 4.1.3 on 2023-01-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0006_event_slot_left"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="space_capacity",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]