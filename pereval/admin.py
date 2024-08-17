from django.contrib import admin

from .models import *


class CoordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'height',)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'winter', 'summer', 'autumn', 'spring',)


admin.site.register(Pereval)
admin.site.register(Images)
admin.site.register(Coords, CoordsAdmin)
admin.site.register(Level, LevelAdmin)
