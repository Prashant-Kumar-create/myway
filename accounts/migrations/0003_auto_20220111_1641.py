# Generated by Django 3.1.4 on 2022-01-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_Retailer',
            field=models.BooleanField(default=False),
        ),
    ]
