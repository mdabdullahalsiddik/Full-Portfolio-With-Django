from django.shortcuts import render
from .models import About

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    about =  About.objects.get()
    return render(request, 'about.html' , { 'about': about})
def resume(request):
    return render(request, 'resume.html')
def services(request):
    return render(request, 'services.html')
def service_details(request):
    return render(request, 'service-details.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def portfolio_details(request):
    return render(request, 'portfolio-details.html')
def contact(request):
    return render(request, 'contact.html')

