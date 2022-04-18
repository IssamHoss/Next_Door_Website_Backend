from atexit import register
from pickle import READONLY_BUFFER
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(Product)
admin.site.register(Event)
admin.site.register(Facility)
admin.site.register(Article)
admin.site.register(Job)

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_staff')
    search_fields =('email', 'username')
    readonly_fields = ('id', 'date_joined')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)