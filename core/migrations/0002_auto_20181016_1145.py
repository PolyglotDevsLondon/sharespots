# Generated by Django 2.0.8 on 2018-10-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
