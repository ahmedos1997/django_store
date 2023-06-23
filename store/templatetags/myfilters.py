# هذا لكتابة نوع العملة بجانب السعر
from django import template


register = template.Library()


def currency(amount):
    return '{:.2f}'.format(amount) + ' $'

register.filter('currency', currency)