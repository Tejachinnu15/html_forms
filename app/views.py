from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('data is submitted')
    return render(request,'login.html')
def topic(request):
   if request.method=='POST':
        Topicname=request.POST['topic']
         
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()






        return HttpResponse('topic data is inserted')






   return render(request,'topic.html')
