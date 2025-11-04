from django.http      import HttpResponse, JsonResponse
from django.shortcuts import render

import json


def helper_side_panel(request):
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
        "panel_size":panel_size,
    }
    return context

def home(request):
    context = helper_side_panel(request)
    return render(request, "index.html",context)

def abstract(request):
    context = helper_side_panel(request)
    return render(request,"abstract.html",context)

def find(request):
    #Automatically close the accordian tabs
    trad = "none"
    pro  = "none"
    self = "none"

    #If some action is taken
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            #return JsonResponse({"error": "Invalid JSON"}, status=400)
            error_info = {
                "error": "Invalid JSON format",
                "message": str(e),
                "position": f"Line {e.lineno}, Column {e.colno}",
                "raw_body_snippet": request.body[:200].decode("utf-8", errors="replace"),  # show snippet of invalid body
            }
            print("JSON decode error:", error_info)
            return JsonResponse(error_info, status=400)

        traditonal = data.get("trad_content")
        proactive  = data.get("proactive_content")
        self_pres  = data.get("self_content")

        if "trad_leader" in request.POST:
            if traditonal == "none":
                trad = "block"
            else:
                trad = "none"
            pro  = proactive
            self = self_pres

        if "pro_leader" in request.POST:
            if proactive == "none":
                pro = "block"
            else:
                pro = "none"
            trad = traditonal
            self = self_pres

        if "self_leader" in request.POST:
            if self_pres == "none":
                self = "block"
            else:
                self = "none"
            trad = traditonal
            pro = proactive

    #////////////

    #Traditional Leader
    '''
    if "trad_leader" in request.POST:
        trad = "block"

    #Proactice Non-tradition leader
    if "pro_leader"  in request.POST:
        pro = "block"
        
    #Self-preserving non-traditional leader
    if "self_leader" in request.POST:
        self = "block"
    '''
    context = helper_side_panel(request)
    context['trad_leader'] = trad
    context['pro_leader']  = pro
    context['self_leader'] = self
    return render(request,"find.html",context)

def reference(request):
    context = helper_side_panel(request)
    return render(request,"ref.html",context)

def doc_preview(request):
    context = helper_side_panel(request)
    return render(request,"doc_preview.html",context)

def participants(request):
    context = helper_side_panel(request)
    return render(request,"participants.html",context)