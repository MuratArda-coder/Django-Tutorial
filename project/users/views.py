from django.shortcuts import render,redirect
from .forms import UserRegisterForms
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForms()

    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    form = PostForm(request.POST)
    if form.is_valid() : 
        form.save()
        form = PostForm()
    return render(request,'profile.html',{'form':form})


