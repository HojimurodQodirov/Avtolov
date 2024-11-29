# Generated by Django 5.1.3 on 2024-11-29 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledAutoPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_type', models.CharField(choices=[('monthly', 'Monthly'), ('weekly', 'Weekly')], max_length=10)),
                ('refill_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_of_day', models.CharField(blank=True, choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThresholdAutoPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('refill_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]