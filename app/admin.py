from django.contrib import admin
from .models import ImageModel


class imgPanel (admin.ModelAdmin): 
    list_display = ('id','image','upload_at',)

admin.site.register(ImageModel, imgPanel)