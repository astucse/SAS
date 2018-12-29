from django.shortcuts import render,redirect
from urllib.parse import urlparse as u
from .models import Video,Slide,Handout
from account.models import Department,Subject
<<<<<<< HEAD
from django.core.files.storage import FileSystemStorage
from .forms import SlideForm

=======
from itertools import chain
import pafy
>>>>>>> 6460c3adef5bce59181bd8c43cf6d0f1c281d741
# Create your views here.

def extract_id(url): #extracts the youtube id from any given working youtube link
    if url.find('youtu.be') == -1 and (not url.find('&') == -1 or not url.find('?') ==-1):
        url=u(url).query.split('&')[0][2:]
    elif not url.find('youtu.be') == -1:
        url=url[url.find('youtu.be/')+9:]
    return url
def extract_title(url):#extracts the title from  any given working youtube link
    if url.find("youtube.com")==-1:
        url="http://www.youtube.com/watch?v="+url
    import re,requests
    raw_html=requests.get(url).text
    match = re.search('<title>(.*?) - YouTube</title>', raw_html)
    title = match.group(1) if match else 'No title'
    return title
# TODO: ----------------------------------------------
# def extract_description(url):                      -
#     if url.find("youtube.com")==-1:                -
#         url="http://www.youtube.com/watch?v="+url  -
#     import re,requests                             -
#     raw=requests.get(url).text                     -
#     x=raw.find('Description')                      -
#     print(x)                                       -
# ----------------------------------------------------

def view_video(request):
    try:
        id=request.GET.get('id')
        video=pafy.new("https://www.youtube.com/watch?v="+id)
        print(video)
        return render(request,"resources/videos.html",{"id":id,"title":video.title,'other':get_videos(request=request),'dlinks':video.streams,"desc":video.description})
    except:
        pass
        # return render(request,"resources/videos.html",{"id":extract_id("https://www.youtube.com/watch?v="+id),"title":extract_title("https://www.youtube.com/watch?v="+id),'other':get_videos(request=request),'dlinks':pafy.new("https://www.youtube.com/watch?v="+id).streams[0].url})
        return redirect('list_videos')

def add_video(request):
    if request.method == 'POST':
        req=request.POST
        url=req['url']
        dept=req['dept']
        sub=req['sub']
        new_video=Video()
        new_video.url=extract_id(url)
        new_video.name=extract_title(url)
        new_video.department=Department.objects.get(pk=dept)
        new_video.subject=Subject.objects.get(pk=sub)
        new_video.save()
        return redirect('view_video')
    url=""
    return render(request,"resources/add_videos.html",{"url":url,'dept':Department.objects.all(),'sub':Subject.objects.all(),})
# TODO: get related and same tagged videos
# TODO: filter and search on videos
def get_videos(request,n=3,s=0):
    lst=[]
    for i in range(min(n,len(Video.objects.all()))):
        lst.append(Video.objects.all()[i+s])
    print (lst)
    return lst
def search(term): #returns list of possible objects that match search criteria
 a = list(chain(Video.objects.filter(name__icontains=term),Video.objects.filter(subject__name__icontains=term),Video.objects.filter(department__name__icontains=term)))
 return a
def list_videos(request):
    pass
#/////////////////////////////////
# TODO: Validate FILE type and SIZE!!!
def add_slides(request):
    if request.method == 'POST':
        req=request.POST
        url=request.FILES['aslide']
        dept=req['Department']
        sub=req['Subject']
        ne = FileSystemStorage()
        a=ne.save(url.name,url)
        nm=url.name
        ns=Slide()
        ns.file="/Uploads/" + a
        ns.name=nm
        ns.department=Department.objects.get(pk=dept)
        ns.subject=Subject.objects.get(pk=sub)
        ns.save()
    dept = Department.objects.all()
    sub = Subject.objects.all()
    return render(request, 'resources/AddSlides.html',{"dept":dept,"sub":sub})


def list_slides(request):
    r=Slide.objects.all()
    dept = Department.objects.all()
    sub = Subject.objects.all()
    return render(request,'resources/SlideView.html',{'r':r,"dept":dept,"sub":sub})
