from django.views.generic import ListView
from .models import *

class HomeView(ListView):
    model = Posts
    context_object_name = 'all_Posts_list'
    template_name = 'home.html'
