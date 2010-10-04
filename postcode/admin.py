from django.contrib.gis import admin
from models import Postcode

class PostcodeAdmin(admin.GeoModelAdmin):
    list_display = ('code', )
    search_fields = ['code']
    

admin.site.register(Postcode, PostcodeAdmin)