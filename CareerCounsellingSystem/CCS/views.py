from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'CCS/index.html')


def userparameters(request):
    if request.user.is_authenticated:
        return  render(request,'CCS/form.html')
    else:
        redirect('login')


def contact(request):
    return render(request,"CCS/contact.html")


def ourteam(request):
    return render(request,'CCS/team.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'CCS/register.html', {'form': form})




