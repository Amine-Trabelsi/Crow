from django.shortcuts import render
from django.http import Http404
# Create your views here.

def index(request):
    # to do: add context
    context = {
        "Author": "Amine",
    }
    return render(request, "crowApp/index.html", context)