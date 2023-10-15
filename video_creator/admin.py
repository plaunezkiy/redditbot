from django.contrib import admin
from video_creator.models import RedditPostVideo, RedditPost, StockVideo, RedditComment

admin.site.register(RedditPost)
admin.site.register(RedditComment)

admin.site.register(RedditPostVideo)
admin.site.register(StockVideo)
# admin.site.register()
