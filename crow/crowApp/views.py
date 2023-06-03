from django.shortcuts import render
from django.http import Http404
# Create your views here.

from .models import CrowPost

def index(request):
    # to do: add context
    posts = CrowPost.objects.order_by("-published_date")
    context = {
        "Author": "Amine",
        "posts": posts, 
    }
    return render(request, "crowApp/index.html", context)