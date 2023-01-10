# Generated by Django 4.1.3 on 2023-01-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0015_remove_event_paid"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="amount",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="date_created",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="ref",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]
