# Generated by Django 4.2.3 on 2023-08-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
