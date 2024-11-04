# Generated by Django 4.2.15 on 2024-11-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_dish_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpecialHours",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="Date")),
                (
                    "opening_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Opening time"
                    ),
                ),
                (
                    "closing_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Closing time"
                    ),
                ),
                (
                    "is_closed",
                    models.BooleanField(default=False, verbose_name="Closed"),
                ),
            ],
            options={
                "verbose_name": "Special Hour",
                "verbose_name_plural": "Special Hours",
            },
        ),
        migrations.RemoveField(model_name="restaurant", name="open_from",),
        migrations.RemoveField(model_name="restaurant", name="open_until",),
        migrations.CreateModel(
            name="WorkingHours",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day_of_week",
                    models.IntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ],
                        verbose_name="Day of the week",
                    ),
                ),
                ("opening_time", models.TimeField(verbose_name="Opening time")),
                ("closing_time", models.TimeField(verbose_name="Closing time")),
            ],
            options={
                "verbose_name": "Working Hour",
                "verbose_name_plural": "Working Hours",
                "unique_together": {("day_of_week",)},
            },
        ),
        migrations.AddField(
            model_name="restaurant",
            name="special_hours",
            field=models.ManyToManyField(
                blank=True, to="store.specialhours", verbose_name="Special hours"
            ),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="working_hours",
            field=models.ManyToManyField(
                to="store.workinghours", verbose_name="Working hours"
            ),
        ),
    ]
