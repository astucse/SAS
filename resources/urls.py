from django.urls import path,include
from . import views
urlpatterns = [
    path('view_video/',views.view_video,name='view_video'),
    path('add_video/',views.add_video,name='add_video'),
    path('list_videos/',views.list_videos,name='list_videos'),
    path('add_video/',views.add_video,name='add_video'),
    path('view_worksheet/',views.view_worksheet,name='view_worksheet'),
    path('add_worksheet/',views.add_worksheet,name='add_worksheet'),
    path('do_worksheet/',views.do_worksheet,name='do_worksheet'),
    path('slides/',views.list_slides,name='list_materials'),
    path('add_slides/',views.add_slides,name='add_slides'),
    path('handouts/',views.list_handouts,name='list_handouts'),
    path('add_handouts/',views.add_handouts,name='add_handouts'),
    path('nav/',views.nav,name='nav'),
]
