# Generated by Django 4.0.6 on 2022-09-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='images',
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
    ]
