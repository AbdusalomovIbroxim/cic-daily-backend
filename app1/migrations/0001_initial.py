# Generated by Django 4.2.2 on 2023-07-04 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryArticlesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Not given', max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='TeamMembersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField(default=18)),
                ('position', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'team_member',
            },
        ),
        migrations.CreateModel(
            name='AuthorArticlesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.teammembersmodel')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.authorarticlesmodel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.categoryarticlesmodel')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
