# Generated by Django 4.0.4 on 2022-05-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_image_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='tier',
            name='is_original_allowed',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
