# Generated by Django 4.1.5 on 2023-10-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_creator', '0002_redditpost_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditcomment',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockvideo',
            name='preview',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockvideo',
            name='title',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
