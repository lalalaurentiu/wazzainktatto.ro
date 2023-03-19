from django.shortcuts import render
from .models import portofoliu

def home(request):
    template_name = "home.html"
    client_addr = request.META.get('REMOTE_ADDR')
    print(client_addr)
    return render(request, template_name)

def about(request):
    template_name = "about.html"
    return render(request, template_name)

def portofolio(request):
    portofoliu_elements = portofoliu.objects.all()
    context = {
        "portofoliu":portofoliu_elements,
    }
    template_name = "portofoliu.html"
    return render (request, template_name, context)

def info(request):
    template_name = "info.html"
    return render(request, template_name)

def rezervare(request):
    template_name = "rezervare.html"
    return render(request, template_name)
