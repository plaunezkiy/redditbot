from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from video_creator.models import RedditPost, RedditPostVideo, RedditComment, StockVideo


def index(request):
    return render(request, 'video_creator/index.html')


@require_http_methods(['POST'])
def create_video(request):
    data = request.POST
    post, _ = RedditPost.objects.get_or_create(url=data.get('url'))
    comment_urls = data.getlist('commentUrl')
    for comment_url in comment_urls:
        comment, _ = RedditComment.objects.get_or_create(url=comment_url, post=post)
    # regex = r"r\/(.+?)\/comments\/(.+?)\/"
    #     thread, post_id = re.search(regex, self.link).groups()
    # RedditPostVideo.objects.create()
    stock_video = StockVideo.objects.get(pk=data.get('baseClipId'))
    video = RedditPostVideo.objects.create(title=data.get('title'), post=post, stock_video=stock_video)
    
    return redirect('video-detail', video.pk)


def video_page(request, video_id):
    video = RedditPostVideo.objects.get(pk=video_id)
    # base_videos = StockVideo.objects.all()
    data = {
        "post": {
            "text": video.post.text,
            # "screenshot": video.post.screenshot.url,
            # "audio": video.post.audio.path,
        }
    }
    return render(request, 'video_creator/video_detail.html', context={"video": video})


def embed_page(request, post_id, comment_id=None):
    embed = RedditPost.objects.get(uid=post_id)
    if comment_id:
        embed = RedditComment.objects.get(uid=comment_id)
    return render(request, 'video_creator/render_embed.html', {'embed': embed.embed_code})
