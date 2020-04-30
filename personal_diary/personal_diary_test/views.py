from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

def HomePageView(request):
    context = {"image_list" : ["images/1.png"]}
    return render(request, "index.html", context)
