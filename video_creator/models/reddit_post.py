import os
import re
from django.db import models


def get_upload_path(instance, filename):
    return os.path.join(instance.get_path(), filename)


class RedditPost(models.Model):
    url = models.URLField()
    thread = models.SlugField()
    uid = models.SlugField()
    embed_code = models.TextField(blank=True)
    text = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to=get_upload_path, blank=True)
    audio = models.FileField(upload_to=get_upload_path, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            regex = r"r\/(.+?)\/comments\/(.+?)\/"
            thread, post_id = re.search(regex, self.url).groups()
            self.thread = thread
            self.uid = post_id
        super(RedditPost, self).save(*args, **kwargs)

    def get_path(self):
        return os.path.join(self.thread, self.uid)
    
    def __str__(self):
        return f"{self.thread} - {self.uid}"


class RedditComment(models.Model):
    url = models.URLField()
    post = models.ForeignKey(RedditPost, on_delete=models.CASCADE, related_name="comments")
    uid = models.SlugField()
    embed_code = models.TextField(blank=True)
    text = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to=get_upload_path, blank=True)
    audio = models.FileField(upload_to=get_upload_path, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            regex = r"r\/(.+?)\/comments\/(.+?)\/comment/(.+?)\/"
            comment_id = re.search(regex, self.url).group(3)
            self.uid = comment_id
        super(RedditComment, self).save(*args, **kwargs)

    def get_path(self):
        return os.path.join(self.post.get_path(), self.uid)
    
    def __str__(self):
        return f"{self.post} - {self.uid}"
