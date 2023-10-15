from django.db import models


class StockVideo(models.Model):
    title = models.CharField(max_length=150)
    preview = models.ImageField()

    def __str__(self):
        return self.title
