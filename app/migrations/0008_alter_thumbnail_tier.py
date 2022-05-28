# Generated by Django 4.0.4 on 2022-05-28 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_tier_thumbnail_thumbnail_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='tier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnails', to='app.tier'),
        ),
    ]
