# Generated by Django 4.0.2 on 2022-02-23 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Update_profile_doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('department', models.CharField(default='', max_length=30)),
                ('start_time', models.CharField(default='', max_length=20)),
                ('end_time', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=50)),
                ('hospital_name', models.CharField(default='', max_length=50)),
                ('qualification', models.CharField(default='', max_length=100)),
                ('institute', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
