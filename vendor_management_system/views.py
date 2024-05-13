# vendor_management_system/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Vendor Management System API.")
