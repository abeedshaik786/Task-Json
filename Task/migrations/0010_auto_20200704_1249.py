# Generated by Django 2.2.2 on 2020-07-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0009_auto_20200704_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='activity_period',
            field=models.ManyToManyField(blank=True, to='Task.Activity_times'),
        ),
    ]
