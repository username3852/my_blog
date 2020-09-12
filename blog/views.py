from django.shortcuts import render
from blog.models import Post

posts = [
    {'title': 'Book1',
     'author': 'Vincent',
     'date_posted': 2015,
     'content': 'Hahahahhahahaha'},

    {'title': 'Book2',
     'author': 'BookHookVincent',
     'date_posted': 2018,
     'content': 'Hihihihihihihihihih'}
]


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})
