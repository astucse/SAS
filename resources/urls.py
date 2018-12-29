from django.urls import path,include
from . import views
urlpatterns = [
    path('view_video/',views.view_video,name='view_video'),
    path('list_videos/',views.list_videos,name='list_videos'),
    path('videos/add_video',views.add_video,name='add_video')
]
