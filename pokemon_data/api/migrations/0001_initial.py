# Generated by Django 4.1.4 on 2022-12-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkm_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(max_length=100)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
    ]
