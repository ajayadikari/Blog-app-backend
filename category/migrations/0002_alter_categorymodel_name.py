# Generated by Django 5.0.1 on 2024-02-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(default='unknown', max_length=70, unique=True),
        ),
    ]
