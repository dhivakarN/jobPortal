# Generated by Django 3.0 on 2023-04-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobapp', '0003_delete_employeee'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=20)),
            ],
        ),
    ]