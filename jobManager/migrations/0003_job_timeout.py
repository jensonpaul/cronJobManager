# Generated by Django 2.0.2 on 2018-03-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobManager', '0002_auto_20180302_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='timeout',
            field=models.IntegerField(default=3600),
        ),
    ]