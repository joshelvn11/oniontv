# Generated by Django 5.0.4 on 2024-04-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('summary', models.TextField()),
                ('cover_image', models.URLField()),
                ('video_url', models.URLField()),
            ],
        ),
    ]
