# Generated by Django 3.0.7 on 2020-06-29 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='conetnt',
            new_name='content',
        ),
    ]
