from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, "index.html", context)