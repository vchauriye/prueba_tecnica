# Generated by Django 4.1.4 on 2022-12-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='inverted_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]