# Generated by Django 4.2.2 on 2023-07-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_articlemodel_articlesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesmodel',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='articlesmodel',
            name='content',
            field=models.TextField(default='None'),
        ),
    ]