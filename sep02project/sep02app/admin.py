from django.contrib import admin
#from sep02app.models import demo
from .models import Useradd,Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display=("name","email","is_resolved","created_at")
    list_filter=("is_resolved","created_at")
    

# Register your models here.
#admin.site.register(demo)
admin.site.register(Useradd)


admin.site.register(Contact,ContactAdmin)
