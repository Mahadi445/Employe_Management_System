# Generated by Django 4.2.1 on 2023-07-04 09:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Department', '0003_alter_department_status'),
        ('Position', '0003_remove_position_name_position_position_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('date_hired', models.DateField()),
                ('salary', models.FloatField(default=0)),
                ('status', models.BooleanField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Department.department')),
                ('position_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Position.position')),
            ],
        ),
    ]