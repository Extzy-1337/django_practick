from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')  # сначала свежие
    return render(request, 'main/index.html', {'posts': posts})