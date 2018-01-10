from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm


def hello_world(request):
    html_ = """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
  </head>
  <body>
    <div class="text-center">
        <h1>Hello, world!</h1>
    </div>
    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
  </body>
</html>
    """
    return HttpResponse(html_)


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "pages/home.html", context)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "contact_form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "pages/home.html", context)


def about(request):
    context = {
        "title": "About"
    }
    return render(request, "pages/home.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Error")
    return render(request, 'auth/login.html', context)


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
    return render(request, 'auth/register.html', context)
