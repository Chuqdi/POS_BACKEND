# Generated by Django 4.2.1 on 2023-05-19 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_biodata_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="biodata",
            name="background",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.background",
            ),
        ),
        migrations.AlterField(
            model_name="biodata",
            name="nextOfKin",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.nextofdkin",
            ),
        ),
        migrations.AlterField(
            model_name="biodata",
            name="securityQuestions",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.securityquestions",
            ),
        ),
    ]
