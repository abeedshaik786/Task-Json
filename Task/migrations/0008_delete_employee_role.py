# Generated by Django 2.2.2 on 2020-07-04 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0007_employee_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee_role',
        ),
    ]