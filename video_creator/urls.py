from django.urls import path
from video_creator import views


urlpatterns = [
    path('', views.index, name='creator_index'),
    path('create_video/', views.create_video, name='create-video'),
    path('video/<int:video_id>/', views.video_page, name='video-detail'),
    path('embed/<str:post_id>/', views.embed_page, name='embed-page'),
    path('embed/<str:post_id>/<str:comment_id>/', views.embed_page, name='embed-page'),
]
