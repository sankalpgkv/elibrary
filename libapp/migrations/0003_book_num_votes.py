# Generated by Django 2.0.5 on 2018-07-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_votes',
            field=models.IntegerField(default=0),
        ),
    ]
