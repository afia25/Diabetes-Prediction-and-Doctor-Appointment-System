# Generated by Django 3.2.7 on 2022-03-02 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_update_profile_doctor_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Take_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=30)),
                ('user_name', models.CharField(default='', max_length=30)),
                ('full_name', models.CharField(default='', max_length=30)),
                ('contact_number', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=20)),
                ('message', models.CharField(default='', max_length=20)),
            ],
        ),
    ]