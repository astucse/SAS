from django.shortcuts import render
from urllib.parse import urlparse as u
from .models import Video,Slide,Handout
from account.models import Department,Subject
# Create your views here.

def videos(request,url="youtube.com/watch?v=QaTIt1C5R-M"):
    return render(request,"resources/videos.html",{"url":url})
def add_video(request):
    if request.method == 'POST':
        req=request.POST
        url=req.get("url","")
        if url.find('youtu.be') == -1:
            url=u(url).query.split('&')[0][2:]
        else:
            url=url[url.find('youtu.be/')+9:]
        print(url)
        return render(request,"resources/videos.html",{"url":url})
    url=""
    return render(request,"resources/add_videos.html",{"url":url,'dept':Department.objects.all(),'sub':Subject.objects.all()})
