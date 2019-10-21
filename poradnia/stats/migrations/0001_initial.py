# Generated by Django 1.11.2 on 2017-08-04 01:20
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        db_index=True, max_length=50, verbose_name="Metric key"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "last_updated",
                    models.DateTimeField(verbose_name="Time to get the last value"),
                ),
            ],
            options={
                "ordering": ["key"],
                "verbose_name": "key",
                "verbose_name_plural": "keys",
            },
        ),
        migrations.CreateModel(
            name="Value",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(default=django.utils.timezone.now)),
                ("value", models.IntegerField()),
                ("comment", models.CharField(max_length=150)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stats.Item"
                    ),
                ),
            ],
            options={
                "ordering": ["item", "time"],
                "verbose_name": "Value",
                "verbose_name_plural": "Values",
            },
        ),
    ]
