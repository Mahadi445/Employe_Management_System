# Generated by Django 4.2.1 on 2023-07-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Position', '0002_alter_position_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='name',
        ),
        migrations.AddField(
            model_name='position',
            name='position_name',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]