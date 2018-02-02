from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            print("Error")
    return render(request, 'accounts/login.html', context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User = get_user_model()
        newUser = User.objects.create_user(username=username, email=email, password=password)
        print(newUser)
        return redirect("/")
    return render(request, 'accounts/register.html', context)
