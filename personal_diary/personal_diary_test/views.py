from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

def HomePageView(request):
    return render(request, "index.html")
