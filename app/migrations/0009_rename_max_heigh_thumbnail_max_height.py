# Generated by Django 4.0.4 on 2022-05-29 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_thumbnail_tier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thumbnail',
            old_name='max_heigh',
            new_name='max_height',
        ),
    ]
