# Generated by Django 2.1.7 on 2019-06-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190621_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Issue',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]