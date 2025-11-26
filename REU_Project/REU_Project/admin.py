from django.contrib import admin
from .models        import Profile, Download, PageView


admin.site.register(PageView)
admin.site.register(Download)
admin.site.register(Profile)