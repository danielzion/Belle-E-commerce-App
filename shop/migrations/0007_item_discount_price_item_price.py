# Generated by Django 4.0.6 on 2022-10-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_image_item_images_item_images1'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]