# Generated by Django 2.2 on 2020-07-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
