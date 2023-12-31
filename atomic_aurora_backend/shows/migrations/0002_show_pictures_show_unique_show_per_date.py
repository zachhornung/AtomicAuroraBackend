# Generated by Django 4.2.5 on 2023-10-13 03:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pictures", "0001_initial"),
        ("shows", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="show",
            name="pictures",
            field=models.ManyToManyField(to="pictures.picture"),
        ),
        migrations.AddConstraint(
            model_name="show",
            constraint=models.UniqueConstraint(fields=("name", "show_date"), name="unique_show_per_date"),
        ),
    ]
