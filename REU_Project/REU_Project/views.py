from django.http      import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, Django is working!")
    return render(request, "index.html")

def abstract(request):
    return render(request,"abstract.html")

def find(request):
    return render(request,"find.html")

def reference(request):
    return render(request,"ref.html")

def doc_preview(request):
    return render(request,"doc_preview.html")