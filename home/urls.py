from django.urls import path
from .views import home, about, portofolio, info, rezervare
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("portofoliu/", portofolio, name="portofoliu"),
    path("info/", info, name="info"),
    path("rezervare/", rezervare, name="rezervare"),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]