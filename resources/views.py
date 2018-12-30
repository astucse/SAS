from django.shortcuts import render,redirect
from urllib.parse import urlparse as u
from .models import Video,Slide,Handout,Question,Choice
from account.models import Department,Subject
from django.core.files.storage import FileSystemStorage
from .forms import SlideForm
from itertools import chain
import pafy

# Create your views here.

def view_video(request):
    try:
        id=request.GET.get('id')
        video=pafy.new("https://www.youtube.com/watch?v="+id)
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
        vid=pafy.new(url)
        new_video.url=vid.videoid
        new_video.name=vid.title
        new_video.department=Department.objects.get(pk=dept)
        new_video.subject=Subject.objects.get(pk=sub)
        new_video.save()
        return redirect('view_video')
    url=""
    return render(request,"resources/add_videos.html",{"url":url,'dept':Department.objects.all(),'sub':Subject.objects.all(),})

def list_videos(request):
    if request.method=='POST':
        context={
        'dept':Department.objects.all(),
        'sub':Subject.objects.all(),
        'vids':search(request.POST.get('bar','')),
        'term':request.POST.get('bar',''),
        }
        return render(request,"resources/list_videos.html",context=context)
    context={'dept':Department.objects.all(),'sub':Subject.objects.all(),'vids':Video.objects.all()}
    return render(request,"resources/list_videos.html",context=context)

def do_worksheet(request):
    pass
def view_worksheet(request):
    context={
    'chap_choices':Question.objects.order_by().values_list('chapter').distinct(),
    }
    if request.method == 'POST':
        context['chap']=request.POST.get("chap_choice","")
        context['data']=enumerate(Question.objects.filter(chapter=context['chap']),1)
        # TODO: CHECK IF ANSWER IS CORRECT
    #     context["v"]=[]
    #     for i,j in request.POST.lists():
    #         try:
    #             # print(Question.objects.filter(id=i))
    #             q=Question.objects.filter(id=i)
    #             context[i+"_v"]="Wrong"
    #             if q.answer == Choice.objects.filter(id=context[i]):
    #                 context["v"].append("Correct")
    #             else:
    #                 context["v"].append("Wrong")
    #         except Exception as x:
    #             # print(x)
    #             pass
    # print(context)
    return render(request,"resources/view_worksheet.html",context)

def add_worksheet(request):
    context={'dept':Department.objects.all(),'sub':Subject.objects.all(),'range4':range(4),'vids':Video.objects.all(),'types':(('Multiple Choice','MC'),('Short Answer','SA'),('True or False','TF'),('Fill in the blanks','FITB'))}
    if request.method=="POST":
        try:
            context['dept_choice']=Department.objects.get(pk=request.POST.get("dept",""))
            context['sub_choice']=Subject.objects.get(pk=request.POST.get("sub",""))
            context['chap_choice']=request.POST.get("chap","")
            context['q_type_choice']=request.POST.get("q_type","")
            context['q_text_choice']=request.POST.get("q_text","")
            if not request.POST.get("choiceAnswer","") == "":
                print(request.POST)
                q=Question()
                q.department=Department.objects.get(id=request.POST.get("dept",""))
                q.subject=Subject.objects.get(id=request.POST.get("sub",""))
                q.chapter=request.POST.get("chap","")
                q.type=request.POST.get("q_type","")
                q.question_text=request.POST.get("q_text","")
                q.hint=request.POST.get("hint","")
                q.explanation=request.POST.get("explain","")
                q.save()
                cA=Choice()
                cA.choice_text=request.POST.get("choiceAnswer","")
                cA.question=q
                cA.answer_to=q
                if request.POST.get("q_type","") == 'MC':
                    c2=Choice()
                    c2.choice_text=request.POST.get("choice2","")
                    c2.question=q
                    c3=Choice()
                    c3.choice_text=request.POST.get("choice3","")
                    c3.question=q
                    c4=Choice()
                    c4.choice_text=request.POST.get("choice4","")
                    c4.question=q
                    c2.save()
                    c3.save()
                    c4.save()
                cA.save()
                del context['chap_choice']
                del context['q_type_choice']
                del context['q_text_choice']
                print(context)
        except Exception as x:
            print(x)
    return render(request,"resources/add_worksheet.html" ,context=context)

#####################################################################################################################
# TODO: get related and same tagged videos
# TODO: filter and search on videos

def get_videos(request,n=3,s=0):
    lst=[]
    for i in range(min(n,len(Video.objects.all()))):
        lst.append(Video.objects.all()[i+s])
    return lst

def search(term): #returns list of video query_set that match search criteria
    a = list(chain(Video.objects.filter(name__icontains=term),Video.objects.filter(subject__name__icontains=term),Video.objects.filter(department__name__icontains=term)))
    return a
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
#<<<<<<< HEAD
#=======

#////////////////////////////////////////////////////////////////////////////////////////////

def add_handouts(request):
    if request.method == 'POST':
        req=request.POST
        url=request.FILES['aslide']
        dept=req['Department']
        sub=req['Subject']
        sec=req['sec']
        ne = FileSystemStorage()
        a=ne.save(url.name,url)
        nm=url.name
        ns=Handout()
        ns.file="/Uploads/" + a
        ns.name=nm
        ns.section=sec
        ns.department=Department.objects.get(pk=dept)
        ns.subject=Subject.objects.get(pk=sub)
        ns.save()
    dept = Department.objects.all()
    sub = Subject.objects.all()
    return render(request, 'resources/AddHandouts.html',{"dept":dept,"sub":sub})

def list_handouts(request):
    r=Handout.objects.all()
    dept = Department.objects.all()
    sub = Subject.objects.all()
    return render(request,'resources/HandoutView.html',{'r':r,"dept":dept,"sub":sub})
