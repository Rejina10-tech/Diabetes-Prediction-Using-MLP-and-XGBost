# Generated by Django 4.2.7 on 2023-11-23 07:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prediction", "0008_alter_predict_proabability"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predict",
            name="age",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(70),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="bmi",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(50.0),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="diabetesPedigree",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0.01),
                    django.core.validators.MaxValueValidator(1.2),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="glucose",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(10),
                    django.core.validators.MaxValueValidator(100),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="insulin",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(100),
                    django.core.validators.MaxValueValidator(1000),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="pregnancy",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(7),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="predict",
            name="skinThickness",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(100),
                    django.core.validators.MaxValueValidator(200),
                ]
            ),
        ),
    ]
