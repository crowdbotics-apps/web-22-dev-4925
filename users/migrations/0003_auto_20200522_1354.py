# Generated by Django 2.2.12 on 2020-05-22 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200522_1337"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="ghghg",),
        migrations.RemoveField(model_name="user", name="hghg",),
    ]
