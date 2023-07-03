from django.urls import path
from checkout import views
from checkout import webhook
from paypal.standard.ipn.views import ipn
urlpatterns = [
    path('stripe/config', views.stripe_config, name='checkout.stripe_config'),
    path('stripe/webhook', webhook.stripe_webhook),
    path('stripe', views.stripe_transaction, name='checkout.stripe'),
    path('paypal', views.paypal_transaction, name='checkout.paypal'),
    path('paypal/webhook', ipn, name='checkout.paypal-webhook'),

]


