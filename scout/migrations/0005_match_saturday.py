# Generated by Django 2.0.3 on 2018-03-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0004_auto_20180331_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
    ]