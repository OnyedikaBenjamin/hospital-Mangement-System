from django.contrib import admin

# Register your models here.
from . models import User

admin.site.register(User)
admin.site.site_header  =  "Don Royale Hospital"  
admin.site.site_title  =  "Don Royale Hospital" 
# admin.site.index_title  = "Don Royale Hospital" 