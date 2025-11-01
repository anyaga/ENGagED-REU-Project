from django.http      import HttpResponse
from django.shortcuts import render



def helper_side_panel(request,action):
    display_value = "none"
    panel_size = "0em"
    if "about-open" in request.POST:
        display_value = "block"
    if "about-close" in request.POST:
        display_value = "none"
    if 'table_of_contents' in request.POST:
        panel_size = "20em"
    if 'table_close' in request.POST:
        panel_size = "0em"
    context = {
        "display_value":display_value,
        "action": action,
        "panel_size":panel_size,
    }
    return context

def home(request,action="close"):
    context = helper_side_panel(request,action)
    return render(request, "index.html",context)

def abstract(request,action):
    context = helper_side_panel(request,action)
    return render(request,"abstract.html",context)

def find(request,action):
    print("action: "+action)
    print(request.POST)
    trad = "none"
    pro = "none"
    self = "none"
    #Traditional Leader
    if "trad_leader" in request.POST:
        trad = "block"

    #Proactice Non-tradition leader
    if "pro_leader"  in request.POST:
        pro = "block"
        
    #Self-preserving non-traditional leader
    if "self_leader" in request.POST:
        self = "block"

    context = helper_side_panel(request,action)
    context['trad_leader'] = trad
    context['pro_leader']  = pro
    context['self_leader'] = self
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