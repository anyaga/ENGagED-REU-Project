from django.http      import HttpResponse
from django.shortcuts import render



def helper_side_panel(request,action):
    display_value = "none"
    if "about-open" in request.POST:
        display_value = "block"
    if "about-close" in request.POST:
        display_value = "none"
    context = {
        "display_value":display_value,
        "action": action,
    }
    return context

def home(request,action="close"):
    print("action" + str(action))
    context = helper_side_panel(request,action)
    return render(request, "index.html",context)

def abstract(request,action):
    context = helper_side_panel(request,action)
    return render(request,"abstract.html",context)

def find(request,action):
    context = helper_side_panel(request,action)
    return render(request,"find.html",context)

def reference(request,action):
    context = helper_side_panel(request,action)
    return render(request,"ref.html",context)

def doc_preview(request,action):
    context = helper_side_panel(request,action)
    return render(request,"doc_preview.html",context)

def participants(request,action):
    context = helper_side_panel(request,action)
    return render(request,"participants.html",context)