# Generated by Django 2.0.5 on 2018-05-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('exchange', models.CharField(max_length=255)),
                ('base', models.CharField(max_length=255)),
                ('quote', models.CharField(max_length=255)),
                ('track', models.CharField(max_length=255)),
                ('peg', models.CharField(max_length=255)),
                ('tolerance', models.FloatField()),
                ('fee', models.FloatField()),
                ('order_amount', models.FloatField()),
                ('total_bid', models.FloatField()),
                ('total_ask', models.FloatField()),
            ],
        ),
    ]
