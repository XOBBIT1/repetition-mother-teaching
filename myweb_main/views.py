from django.shortcuts import render, redirect
from myweb_main.forms.post import PostForm
from myweb_main.forms.reg import RegistrationForm
from .models import Post

def index(request):
    return render(request, "myweb_main/index.html")

def post_page(request):
    error = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("about")
        else:
            error = "Форма не верна"
    form = PostForm()
    context = {
         "form": form,
         "error": error
    }
    return render(request, 'myweb_main/post.html', context)


def about(request):
    posts = Post.objects.order_by('-id')
    return render(request, "myweb_main/index_about.html", {'title': 'Публикации', 'posts': posts})

def reg_page(request):
    error = ''
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма не верна"
    form = RegistrationForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'myweb_main/reg.html', context)
