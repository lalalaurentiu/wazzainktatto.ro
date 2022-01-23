from django.urls import path
from .views import home, about, portofolio, info, rezervare

app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("portofoliu/", portofolio, name="portofoliu"),
    path("info/", info, name="info"),
    path("rezervare/", rezervare, name="rezervare")
]