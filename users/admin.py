from django.contrib import admin
from .models import *


class PassUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastname', 'firstname', 'surname', 'phone', 'email',)


admin.site.register(PassUser, PassUserAdmin)
