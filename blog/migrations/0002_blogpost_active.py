# Generated by Django 5.1.4 on 2024-12-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
