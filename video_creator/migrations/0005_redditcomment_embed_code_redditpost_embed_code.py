# Generated by Django 4.1.5 on 2023-10-15 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_creator', '0004_alter_redditcomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditcomment',
            name='embed_code',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='redditpost',
            name='embed_code',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
