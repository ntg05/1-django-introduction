# Generated by Django 4.2.15 on 2024-11-04 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_alter_workinghours_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="specialhours",
            unique_together={("date", "opening_time", "closing_time", "is_closed")},
        ),
    ]
