from django.http      import HttpResponse
from django.shortcuts import render



def helper_side_panel(action):
    if action == "open":
        panel_size = "250px"
    else:
        panel_size = "0px"
    context = {
        "panel_size": panel_size,
        "action": action,

    }
    return context

def home(request,action="close"):
    context = helper_side_panel(action)
    return render(request, "index.html",context)

def abstract(request,action):
    context = helper_side_panel(action)
    return render(request,"abstract.html",context)

def find(request,action):
    context = helper_side_panel(action)
    return render(request,"find.html",context)

def reference(request,action):
    context = helper_side_panel(action)
    return render(request,"ref.html",context)

def doc_preview(request,action):
    context = helper_side_panel(action)
    return render(request,"doc_preview.html",context)

def participants(request,action):
    context = helper_side_panel(action)
    return render(request,"participants.html",context)