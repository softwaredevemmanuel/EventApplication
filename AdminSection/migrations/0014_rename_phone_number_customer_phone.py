# Generated by Django 4.1.3 on 2023-01-06 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AdminSection", "0013_rename_event_name_customer_event_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer", old_name="phone_number", new_name="phone",
        ),
    ]