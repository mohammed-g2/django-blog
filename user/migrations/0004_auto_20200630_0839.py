# Generated by Django 3.0.7 on 2020-06-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200630_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default="This user did'nt provide any information", max_length=256),
        ),
    ]