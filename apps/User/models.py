from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PlasticCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plastic_cards')
    card_number = models.CharField(max_length=16, unique=True)
    expiration_date = models.CharField(max_length=5)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Card ending in {self.card_number}"


class House(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owners = models.ManyToManyField(User, related_name='houses')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
