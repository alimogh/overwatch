# Generated by Django 2.1.5 on 2019-11-23 00:17

from django.db import migrations, models
import overwatch.models.bot


class Migration(migrations.Migration):

    dependencies = [
        ('overwatch', '0037_auto_20191122_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='name',
            field=models.CharField(help_text='Name to identify this bot. Usually the name of the pair it operates on', max_length=255, validators=[overwatch.models.bot.no_slash]),
        ),
    ]