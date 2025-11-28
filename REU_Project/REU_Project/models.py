from django.db import models


class Profile(models.Model):
    image                 = models.ImageField(upload_to='avatar/', blank=True, null=True)
    name                  = models.CharField(max_length=20)
    identity              = models.CharField(max_length=20)
    professional_position = models.CharField(max_length=20)
    discipline            = models.CharField(max_length=20)
    archetype             = models.CharField(max_length=20)

    def __str__(self):
        sub1 = f"name={self.name}\n identity={self.identity}\n prof={self.professional_position}"
        sub2 = f"discipline={self.discipline}\narchetype={self.archetype}\n\n"
        return sub1 + sub2

#See who downloads my papers
class Download(models.Model):
    email = models.EmailField()
    pdf   = models.CharField(max_length=255)
    time  = models.DateTimeField(auto_now_add=True)

    page_view = models.ForeignKey(PageView, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"email={self.email} downloaded {self.pdf} at {self.time}\n"

#See who views a page
class PageView(models.Model):
    ip_address = models.GenericIPAddressField() #Both IPv4 and IPv6
    timestamp  = models.DateTimeField(auto_now_add=True)
    path       = models.CharField(max_length=255)
    
    ############## Look over this section #################
    user_agent = models.CharField(max_length=255,blank=True,null=True)

    #A User-Agent (often abbreviated UA) is a small text string 
    # that your browser—or any client making an HTTP request—sends 
    # to a website to identify:

    """
        Mozilla/5.0 (Windows NT 10.0; Win64; x64)
        AppleWebKit/537.36 (KHTML, like Gecko)
        Chrome/119.0.0.0 Safari/537.36
    """
    def __str__(self):
        return f"ip-address{self.ip_address}"