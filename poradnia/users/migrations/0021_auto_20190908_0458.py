
# Generated by Django 1.11.24 on 2019-09-08 02:58
from django.contrib.auth import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20190707_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(
                error_messages={
                    'unique': 'A user with that username already exists.'
                },
                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                max_length=150,
                unique=True,
                validators=[
                    validators.UnicodeUsernameValidator()
                ],
                verbose_name='username'
            ),
        ),
    ]
