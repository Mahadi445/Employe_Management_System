# Generated by Django 4.2.1 on 2023-07-04 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employe', '0002_alter_employees_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='middlename',
        ),
    ]