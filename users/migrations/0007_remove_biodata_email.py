# Generated by Django 4.2.1 on 2023-05-19 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_nextofdkin_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="biodata",
            name="email",
        ),
    ]