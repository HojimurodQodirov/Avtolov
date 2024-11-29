from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ThresholdAutoPayment, ScheduledAutoPayment
from apps.User.models import PlasticCard, House
from decimal import Decimal

User = get_user_model()


class AutoPaymentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.card = PlasticCard.objects.create(
            user=self.user,
            card_number='1234567890123456',
            expiration_date='12/25',
            balance=Decimal('200.00')
        )
        self.house = House.objects.create(
            name='Test House',
            address='123 Test St.'
        )
        self.house.owners.add(self.user)

        self.threshold_auto_payment = ThresholdAutoPayment.objects.create(
            user=self.user,
            threshold_amount=Decimal('100.00'),
            refill_amount=Decimal('50.00')
        )

        self.scheduled_auto_payment = ScheduledAutoPayment.objects.create(
            user=self.user,
            schedule_type=ScheduledAutoPayment.MONTHLY,
            refill_amount=Decimal('20.00'),
            time_of_day='morning'
        )

    def test_threshold_auto_payment_refill(self):
        self.card.balance = Decimal('80.00')
        self.card.save()

        if self.card.balance < self.threshold_auto_payment.threshold_amount:
            self.card.balance += self.threshold_auto_payment.refill_amount
            self.card.save()

        self.card.refresh_from_db()
        self.assertEqual(self.card.balance, Decimal('130.00'))

    def test_scheduled_auto_payment_refill(self):
        initial_balance = self.card.balance
        self.scheduled_auto_payment.is_active = True
        self.scheduled_auto_payment.save()

        if self.scheduled_auto_payment.is_active:
            self.card.balance += self.scheduled_auto_payment.refill_amount
            self.card.save()

        self.card.refresh_from_db()
        self.assertEqual(self.card.balance, initial_balance + Decimal('20.00'))

    def test_toggle_threshold_auto_payment(self):
        self.assertTrue(self.threshold_auto_payment.is_active)
        self.threshold_auto_payment.toggle_activation()
        self.assertFalse(self.threshold_auto_payment.is_active)
        self.threshold_auto_payment.toggle_activation()
        self.assertTrue(self.threshold_auto_payment.is_active)

    def test_toggle_scheduled_auto_payment(self):
        self.assertTrue(self.scheduled_auto_payment.is_active)
        self.scheduled_auto_payment.toggle_activation()
        self.assertFalse(self.scheduled_auto_payment.is_active)
        self.scheduled_auto_payment.toggle_activation()
        self.assertTrue(self.scheduled_auto_payment.is_active)
