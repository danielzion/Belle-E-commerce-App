# Generated by Django 4.0.6 on 2022-10-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'lbl pr-label1'), ('H', 'lbl pr-label2'), ('S', 'lbl on-sale'), ('P', 'lbl pr-label3')], max_length=1),
        ),
    ]
