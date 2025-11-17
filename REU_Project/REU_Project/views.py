from django.http       import HttpResponse, JsonResponse, FileResponse
from django.core.files import File
from django.conf       import settings
from django.shortcuts  import render
from .models           import Profile, Download
from .forms            import download_form

import json

def helper_side_panel(request):
    display_value = "none"
    profile_value = "none"
    panel_size = "0em"
    if "about-open" in request.POST:
        display_value = "block"
    if "about-close" in request.POST:
        display_value = "none"
    if 'table_of_contents' in request.POST:
        panel_size = "15em"
    if 'table_close' in request.POST:
        panel_size = "0em"
    if "profile-open" in request.POST:
        profile_value = "block"
    context = {
        "display_value":display_value,
        "profile_value":profile_value,
        "panel_size":panel_size,
    }
    return context

def home(request):
    context = helper_side_panel(request)
    return render(request, "index.html",context)

def abstract(request):
    if request.method == 'POST':
        form = download_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            Download.objects.create(email=email)


    context = helper_side_panel(request)
    return render(request,"abstract.html",context)

def find(request):
    #Automatically close the accordian tabs
    trad = "none"
    pro  = "none"
    self = "none"
    #If some action is taken
    if request.method == "POST" and "profile-open" not in request.POST and "about-open" not in request.POST and "about-close" not in request.POST  and "table_close" not in request.POST and "table_of_contents" not in request.POST:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            error_info = {
                "error": "Invalid JSON format",
                "message": str(e),
                "position": f"Line {e.lineno}, Column {e.colno}",
                "raw_body_snippet": request.body[:200].decode("utf-8", errors="replace"),  # show snippet of invalid body
            }
            print("JSON decode error:", error_info)
            return JsonResponse(error_info, status=400)
        traditonal = data.get("trad_content","none")
        proactive  = data.get("proactive_content","none")
        self_pres  = data.get("self_content","none")
        button = data.get("button")


        if button == "trad_leader":
            if traditonal == "none":
                trad = "block"
            else:
                trad = "none"
            pro  = proactive
            self = self_pres

        if button == "pro_leader":
            if proactive == "none":
                pro = "block"
            else:
                pro = "none"
            trad = traditonal
            self = self_pres

        if button == "self_leader":
            if self_pres == "none":
                self = "block"
            else:
                self = "none"
            trad = traditonal
            pro = proactive
    context = helper_side_panel(request)
    context['trad_leader'] = trad
    context['pro_leader']  = pro
    context['self_leader'] = self
    print(context)
    return render(request,"find.html",context)

def reference(request):
    context = helper_side_panel(request)
    return render(request,"ref.html",context)

def doc_preview(request):
    if request.method == 'POST':
        form = download_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Download.objects.create(email=email)

    context = helper_side_panel(request)
    return render(request,"doc_preview.html",context)

def create_participants(request):
    if not Profile.objects.filter(name="Killua").exists():
        person1 = Profile(name="Killua",
                        identity="Black Male",
                        professional_position="Graduate School",
                        discipline="Mechanical",
                        archetype="Proactive")
        person1.image.name = "img/masc1.png"
        person1.save()

    if not Profile.objects.filter(name="Dad").exists():
        person2 = Profile(name="Dad",
                        identity="Black/Hispanic Male",
                        professional_position="Young Professional",
                        discipline="Mechanical",
                        archetype="Proactive")  
        person2.image.name = "img/masc3.png"
        person2.save()
    if not Profile.objects.filter(name="Jae").exists():
        person3 = Profile(name="Jae",
                        identity="Black Female",
                        professional_position="Young Professional",
                        discipline="Civil",
                        archetype="Self-Preserving")
        person3.image.name = "img/masc2.png"
        person3.save()
    if not Profile.objects.filter(name="Gabrielle").exists():
        person4 = Profile(name="Gabrielle",
                        identity="Black Female",
                        professional_position="Young Professional",
                        discipline="Chemical",
                        archetype="Traditional")
        person4.image.name = "img/fem1.png"
        person4.save()
    if not Profile.objects.filter(name="Jesica").exists():
        person5 = Profile(name="Jesica",
                        identity="Black Femme Presenting",
                        professional_position="Young Professional",
                        discipline="Industrial",
                        archetype="Traditional")
        person5.image.name = "img/fem2.png"
        person5.save()
    return HttpResponse("People created succesfully")

def participants(request):
    create_participants(request)
    context = helper_side_panel(request)
    profile_open = "none"
    profile    = None
    image      = None
    name       = None
    identity   = None
    profession = None
    discipline = None
    archetype  = None
    

    if "Killua" in request.POST:
        profile = Profile.objects.get(name="Killua")
        image =  "img/masc1.png"


    if "Dad" in request.POST:
        profile = Profile.objects.get(name="Dad")
        image =  "img/masc3.png"

    if "Jae" in request.POST:
        profile = Profile.objects.get(name="Jae")
        image =  "img/masc2.png"

    if "Gabrielle" in request.POST:
        profile = Profile.objects.get(name="Gabrielle")
        image =  "img/fem1.png"

    if "Jesica" in request.POST:
        profile = Profile.objects.get(name="Jesica")
        image =  "img/fem2.png"

    if profile is not None:
        
        name      = profile.name
        #image     = profile.image.name
        identity  = profile.identity
        profession = profile.professional_position
        discipline = profile.discipline
        archetype  = profile.archetype   
        profile_open = "block" #check this  

        print("iamge:")
        print(image)

    if "about-close" in request.POST:
        profile_open = "none"

    context["profile_open"] = profile_open
    context['image']      = image
    context["name"]       = name
    context["identity"]   = identity
    context["profession"] = profession
    context["discipline"] = discipline
    context["archetype"]  = archetype

    return render(request,"participants.html",context)