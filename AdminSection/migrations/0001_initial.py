# Generated by Django 4.2.3 on 2023-07-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('event_id', models.CharField(max_length=100)),
                ('ref', models.CharField(max_length=200, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': (),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('space_capacity', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('event_end_date', models.DateTimeField(blank=True, null=True)),
                ('bookings', models.IntegerField(default=0)),
                ('slot_left', models.IntegerField(default=0)),
                ('header_images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('is_cancelled', models.BooleanField(default=False)),
            ],
        ),
    ]
