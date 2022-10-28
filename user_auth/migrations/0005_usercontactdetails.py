# Generated by Django 4.1.2 on 2022-10-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('linkdin', models.CharField(blank=True, max_length=300)),
                ('facebook_name', models.CharField(blank=True, max_length=300)),
                ('twitter_name', models.CharField(blank=True, max_length=300)),
                ('instagram', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]