from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import ThresholdAutoPayment, ScheduledAutoPayment
from apps.User.models import PlasticCard, House


@receiver(post_save, sender=ThresholdAutoPayment)
def handle_threshold_autopayment(sender, instance, **kwargs):
    card = PlasticCard.objects.filter(user=instance.user).first()
    house = House.objects.filter(owners=instance.user).first()

    if not card or not house:
        return

    if instance.is_active:
        if card.balance >= instance.refill_amount:
            card.balance -= instance.refill_amount
            card.save()
            house.balance += instance.refill_amount
            house.save()
            print(
                f"AutoPayment successful: {instance.refill_amount} transferred from card {card.card_number[-4:]} to house {house.name}.")
        else:
            raise ValidationError("Insufficient funds on the card for threshold auto-payment.")


@receiver(post_save, sender=ScheduledAutoPayment)
def handle_scheduled_autopayment(sender, instance, **kwargs):
    card = PlasticCard.objects.filter(user=instance.user).first()
    house = House.objects.filter(owners=instance.user).first()

    if not card or not house:
        return

    if instance.is_active:
        if card.balance >= instance.refill_amount:
            card.balance -= instance.refill_amount
            card.save()
            house.balance += instance.refill_amount
            house.save()
            print(
                f"Scheduled AutoPayment successful: {instance.refill_amount} transferred from card {card.card_number[-4:]} to house {house.name}.")
        else:
            raise ValidationError("Insufficient funds on the card for scheduled auto-payment.")
