# Generated by Django 2.1.5 on 2019-12-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatch', '0046_auto_20191211_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='botbalance',
            name='bid_available_as_base',
            field=models.FloatField(blank=True, null=True),
        ),
    ]