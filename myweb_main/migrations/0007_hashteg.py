# Generated by Django 3.2.9 on 2021-12-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb_main', '006_add_profile_instance_to_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTeg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('post', models.ManyToManyField(to='myweb_main.Post')),
            ],
        ),
    ]