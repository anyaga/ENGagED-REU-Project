from django.http      import HttpResponse, JsonResponse
from django.shortcuts import render
from .models          import Profile

import json


def helper_side_panel(request):
    display_value = "none"
    panel_size = "0em"
    if "about-open" in request.POST:
        display_value = "block"
    if "about-close" in request.POST:
        display_value = "none"
    if 'table_of_contents' in request.POST:
        panel_size = "15em"
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

def create_participants(request):
    person1 = Profile(name="Killua",
                    identity="Black Male",
                    professional_position="Graduate School",
                    discipline="Mechanical",
                    archetype="Proactive")
    person1.save()

    person2 = Profile(name="Dad",
                    identity="Black/Hispanic Male",
                    professional_position="Young Professional",
                    discipline="Mechanical",
                    archetype="Proactive")  
    person2.save()

    person3 = Profile(name="Jae",
                    identity="Black Female",
                    professional_position="Young Professional",
                    discipline="Civil",
                    archetype="Self-Preserving")
    person3.save()

    person4 = Profile(name="Gabrielle",
                    identity="Black Female",
                    professional_position="Young Professional",
                    discipline="Chemical",
                    archetype="Traditional")
    person4.save()

    person5 = Profile(name="Jesica",
                    identity="Black Femme Presenting",
                    professional_position="Young Professional",
                    discipline="Industrial",
                    archetype="Traditional")
    person5.save()




def participants(request):
    create_participants(request)
    profs = Profile.objects.all()
    
    context = helper_side_panel(request)
    profile_open = "none"

    profs = Profile.objects.all()

    if "participants-name" in request.POST:
        profile_open = "block" #check this
        print("NONE")
    if "about-close" in request.POST:
        profile_open = "none"
    context["profile_open"] = profile_open
    return render(request,"participants.html",context)