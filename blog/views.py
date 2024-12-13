from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import BlogPost
from blog.forms import BlogForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    posts = BlogPost.objects.all()
    print(posts)
    context = {
        "posts": posts
    }
    return render(request, "index.html", context)

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {
        "post": post,
    }
    return render(request, "post_detail.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def pricing(request):
    return render(request, "pricing.html")

def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            date = form.cleaned_data.get("date")

            print(title)
            print(content)
            print(date)

            BlogPost.objects.create(
                title=title,
                content=content,
                published_date=date
            )

            return redirect("/")
    
    else:
        form = BlogForm()

    context = {
        "form": form,
    }
    return render(request, "create_post.html", context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "Invalid username or password")

    else:
        form = LoginForm()

    context = {
        "form": form
    }
    return render(request, "login_view.html", context)

def logout_view(request):
    logout(request)
    return redirect("login_view")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            confirm_password = form.cleaned_data.get("confirm_password")

            if password != confirm_password:
                form.add_error("confirm_password", "Passwords do not match")
                return render(request, "register_view.html", {"form": form})
            
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()

            return redirect("login_view")

            
    else:
        form = RegisterForm()
    context = {
        "form":form
    }
    return render(request, "register_view.html", context)




def home_view(request):
    context = {
        "name": None,
        "user_age": 25,
        "languages": ["Python", "Django", "Javascript"]
    }
    return render(request, "old/home.html", context)

def hello_world(request):
    context = {
        "user_name": "Destiny",
        "title": "My App",
        "favourite_color": "blue"
    }
    return render(request, "old/hello_world.html", context)

# def about(request):
#     return render(request, "about.html")

# def contact(request):
#     html = "<h1>Contact Page</h1>"
#     return HttpResponse(html)

# def pricing(request):
#     html = "<h1>Pricing Page</h1>"
#     return HttpResponse(html)