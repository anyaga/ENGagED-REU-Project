from django.contrib import admin
from .models        import Profile, Download, PageView

'''
admin.site.register(PageView)
admin.site.register(Download)
admin.site.register(Profile)
'''

#customize how things look in admin database

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('ip_address','viewed_at','path','user_agent')
    search_fields = ('ip_address','viewed_at','user_agent')    
    date_hierarchy = 'viewed_at'
    ordering = ('-viewed_at')


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display  = ('email','pdf_name','downloaded_at')
    search_fields = ('email','pdf_name')
    date_hierarchy = 'downloaded_at'
    ordering       = ('-downloaded_at')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('img','name','identity',
                    'position','discip','archetype')
    search_fields = ('name')
    ordering      = ('-name')