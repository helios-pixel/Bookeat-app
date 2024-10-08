# Generated by Django 5.0.1 on 2024-01-31 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
        ('restaurant', '0006_remove_customerpurchase_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount_paid', models.FloatField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_signature', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.customer')),
                ('resturent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.resturent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerOrderItemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(default=0)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.resturentfooditem')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.customerorderitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
