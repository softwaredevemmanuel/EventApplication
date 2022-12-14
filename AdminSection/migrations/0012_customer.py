# Generated by Django 4.1.3 on 2023-01-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0011_event_is_cancelled"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone_number", models.IntegerField()),
                ("event_name", models.CharField(max_length=100)),
            ],
        ),
    ]
