# Generated by Django 1.9.4 on 2016-04-09 21:34
import django.contrib.sites.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("sites", "0003_auto_20151217_2355")]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="domain",
            field=models.CharField(
                max_length=100,
                unique=True,
                validators=[django.contrib.sites.models._simple_domain_name_validator],
                verbose_name="domain name",
            ),
        )
    ]
