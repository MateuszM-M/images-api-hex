# Generated by Django 4.0.4 on 2022-05-31 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_user_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.tier'),
        ),
    ]
