# Generated by Django 4.0.6 on 2022-10-11 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_item_discount_price_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('H', 'Hot'), ('S', 'Sale'), ('P', 'Popular')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]