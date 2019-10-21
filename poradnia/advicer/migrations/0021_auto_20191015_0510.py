# Generated by Django 2.2.6 on 2019-10-15 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advicer', '0020_auto_20190707_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='advicer',
            field=models.ForeignKey(help_text='Person who give a advice', limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Advicer'),
        ),
    ]
