# Generated by Django 5.0.3 on 2024-04-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_ratingorder_order_alter_ratingorder_order_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingorder',
            name='order_request',
            field=models.TextField(blank=True, null=True, verbose_name='Заявка на заказ'),
        ),
    ]
