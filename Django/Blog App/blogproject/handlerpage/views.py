from django.shortcuts import render
from django.views.defaults import page_not_found

# Create your views here.
# handerpage/views.py 

def handler404(request, exception):
    return page_not_found(request, exception, template_name="404.html")