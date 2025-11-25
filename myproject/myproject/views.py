from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

def member(request):
    return HttpResponse("Hello, Dependra")

def home(request):
    return HttpResponse("Hello, World!")
def about(request):
    return HttpResponse("This is the about page.")
def contact(request):
    return HttpResponse("This is the contact page.")

# templates
def home_template(request):
    return render(request, 'index.html')

def custom_404(request, exception):
    # For DEBUG=False, Django expects the template to be named exactly '404.html'
    # and it should be in the root templates directory
    return render(request, '404.html', status=404)


