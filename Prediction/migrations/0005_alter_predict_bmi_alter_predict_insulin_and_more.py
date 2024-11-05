# Generated by Django 4.2.7 on 2023-11-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prediction", "0004_alter_predict_glucose"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predict",
            name="bmi",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="predict",
            name="insulin",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="predict",
            name="skinThickness",
            field=models.IntegerField(),
        ),
    ]