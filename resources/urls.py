from django.urls import path,include
from . import views
urlpatterns = [
    path('view_video/',views.view_video,name='view_video'),
    path('list_videos/',views.list_videos,name='list_videos'),
<<<<<<< HEAD
    path('videos/add_video/',views.add_video,name='add_video'),
    path('slides/',views.list_slides,name='list_materials'),
    path('slides/add_slides',views.add_slides,name='add_slides'),
=======
    path('add_video/',views.add_video,name='add_video')
>>>>>>> 6460c3adef5bce59181bd8c43cf6d0f1c281d741
]
