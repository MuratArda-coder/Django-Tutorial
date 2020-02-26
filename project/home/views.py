from django.shortcuts import render
from django.views.generic import ListView
from users.models import Post
# Create your views here.

def home(request):
    contex1 = {'post':Post.objects.all()}
    return render(request,'home_page.html',contex1)

class PostlistView(ListView):
    model = Post
    template_name = 'home_page.html'
    context_object_name = 'post'
    ordering = ['-date_published']