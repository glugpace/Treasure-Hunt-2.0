# Generated by Django 3.0.4 on 2020-03-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tsite', '0006_auto_20200327_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='l1_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='l2_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='l3_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='l4_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='l5_time',
            field=models.DateTimeField(null=True),
        ),
    ]
