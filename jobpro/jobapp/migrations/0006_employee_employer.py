# Generated by Django 3.0 on 2023-04-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobapp', '0005_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phNumber', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('education', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmpnyname', models.CharField(max_length=20)),
                ('cmpnyfield', models.CharField(max_length=20)),
                ('phNumber', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
