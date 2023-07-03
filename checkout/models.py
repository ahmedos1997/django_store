from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class TransactionStatus(models.IntegerChoices):
    pending = 0, _('pending'),
    completed = 1, _('completed')



class PaymentMethod(models.IntegerChoices):
    stripe = 1, _('strip'),
    paypal = 2, _('paypal')


class Transaction(models.Model):
    session = models.CharField(max_length=255)
    amount = models.FloatField()
    items = models.JSONField()
    customer = models.JSONField()
    status = models.IntegerField(
        choices=TransactionStatus.choices, default=TransactionStatus.pending
    )

    payment_method = models.IntegerField(
        choices=PaymentMethod.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
