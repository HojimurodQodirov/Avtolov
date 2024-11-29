from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ThresholdAutoPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    threshold_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def toggle_activation(self):
        self.is_active = not self.is_active
        self.save()

    def __str__(self):
        return f"Threshold AutoPayment for {self.user} — Threshold: {self.threshold_amount} — Active: {self.is_active}"


class ScheduledAutoPayment(models.Model):
    MONTHLY = 'monthly'
    WEEKLY = 'weekly'

    SCHEDULE_CHOICES = [
        (MONTHLY, 'Monthly'),
        (WEEKLY, 'Weekly'),
    ]

    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule_type = models.CharField(max_length=10, choices=SCHEDULE_CHOICES)
    refill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_of_day = models.CharField(max_length=10, choices=TIME_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def toggle_activation(self):
        self.is_active = not self.is_active
        self.save()

    def __str__(self):
        return f"{self.schedule_type.capitalize()} AutoPayment for {self.user} — Active: {self.is_active}"
