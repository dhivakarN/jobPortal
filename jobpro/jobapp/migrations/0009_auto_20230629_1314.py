# Generated by Django 3.0 on 2023-06-29 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0008_auto_20230403_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='phNumber',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='employer',
            old_name='cmpnyfield',
            new_name='field',
        ),
        migrations.RenameField(
            model_name='employer',
            old_name='cmpnyname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employer',
            old_name='phNumber',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='jobdetail',
            old_name='compnyNAme',
            new_name='companyName',
        ),
        migrations.RenameField(
            model_name='jobdetail',
            old_name='jobName',
            new_name='name',
        ),
    ]
