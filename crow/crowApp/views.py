from django.shortcuts import render
from django.http import Http404
# Create your views here.

from django.views.generic.list import ListView
from .models import CrowPost

class PostsList(ListView):
    template_name="crowApp/posts.html"
    model = CrowPost
    paginate_by = 2 # No more than 5 posts should be displayed in one page
    ordering = ['-published_date']
