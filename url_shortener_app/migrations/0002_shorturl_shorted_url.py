# Generated by Django 2.2 on 2019-04-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='shorted_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
