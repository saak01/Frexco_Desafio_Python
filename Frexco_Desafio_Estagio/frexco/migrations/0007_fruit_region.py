# Generated by Django 4.0.1 on 2022-01-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frexco', '0006_alter_fruit_name_alter_region_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='region',
            field=models.CharField(default='', max_length=40),
        ),
    ]
