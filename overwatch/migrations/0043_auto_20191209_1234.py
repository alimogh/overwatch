# Generated by Django 2.1.5 on 2019-12-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overwatch', '0042_auto_20191208_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='peg',
            new_name='peg_currency',
        ),
        migrations.RenameField(
            model_name='bot',
            old_name='market_price',
            new_name='use_market_price',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='base',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='track',
        ),
        migrations.AddField(
            model_name='bot',
            name='peg_side',
            field=models.CharField(choices=[('base', 'Base'), ('quote', 'Quote')], default='quote', help_text='Which side of the market pair the peg applies to', max_length=255),
            preserve_default=False,
        ),
    ]
