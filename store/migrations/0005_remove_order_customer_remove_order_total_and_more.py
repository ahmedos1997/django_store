# Generated by Django 4.2 on 2023-06-26 13:54

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
        ('store', '0004_product_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.OneToOneField(null=True, on_delete=store.models.Product, to='checkout.transaction'),
        ),
    ]