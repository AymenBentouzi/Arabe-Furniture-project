from django.urls import path
from core.views import index

appname = "core"



urlpatterns = [
    path('', index, name="index")
]