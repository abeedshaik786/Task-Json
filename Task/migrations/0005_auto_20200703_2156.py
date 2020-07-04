# Generated by Django 2.2.2 on 2020-07-03 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_auto_20200703_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='activity_period',
        ),
        migrations.AddField(
            model_name='activity_times',
            name='activity_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activitys', to='Task.Employee'),
        ),
    ]
