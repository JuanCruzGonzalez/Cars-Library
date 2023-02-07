from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Auto)
admin.site.register(Mensaje)
admin.site.register(Marca)

class SlideAdmin(admin.ModelAdmin):
    list_display=('id', 'imagen', 'titulo', 'sub_titulo')

admin.site.register(Slide, SlideAdmin)
