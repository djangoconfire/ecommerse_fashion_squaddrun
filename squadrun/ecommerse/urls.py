from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^upload_image/$',UploadImage,name="upload_image"),
    
]