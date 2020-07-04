# Generated by Django 2.2.2 on 2020-07-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0008_delete_employee_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='activity_period',
        ),
        migrations.AddField(
            model_name='employee',
            name='activity_period',
            field=models.ManyToManyField(blank=True, null=True, to='Task.Activity_times'),
        ),
    ]