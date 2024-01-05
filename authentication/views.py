from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .forms import CutomUserCreationForm

from django.contrib.auth.models import User


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, 
                                username=username, 
                                password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                msg = "Invalid password"
                context['error_msg'] = msg
        except Exception as e:
            print(e,"<<<<<<<<<<<<<<<<<<<<<")
            msg = "Wrong username"
            context['error_msg'] = msg
    return render(request,
                  'authentication/sign-in.html',
                  context
                  )


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    context['page_title'] = "Sign-Up"
    form = CutomUserCreationForm
    if request.method == 'POST':
        form = CutomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    context['form'] = form
    return render(request,
                  'authentication/sign-up.html',
                  context)


def user_logout(request):
    logout(request)
    return redirect('sign_in')


@login_required(login_url='sign_in')
def home(request):
    return render(request,'authentication/home.html')