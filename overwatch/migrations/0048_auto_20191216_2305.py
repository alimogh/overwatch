# Generated by Django 2.1.5 on 2019-12-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatch', '0047_botbalance_bid_available_as_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='botprice',
            name='base_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='botprice',
            name='quote_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
