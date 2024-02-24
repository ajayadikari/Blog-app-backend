# Generated by Django 5.0.1 on 2024-02-07 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
        ('category', '0001_initial'),
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no title', max_length=255)),
                ('total_likes', models.IntegerField(default=0)),
                ('total_reports', models.IntegerField(default=0)),
                ('report_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.authormodel')),
                ('category', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='category.categorymodel')),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='liked_posts', to='reader.readermodel')),
                ('reports', models.ManyToManyField(blank=True, null=True, related_name='reported_posts', to='reader.readermodel')),
            ],
        ),
    ]
