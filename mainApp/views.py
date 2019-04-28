from django.shortcuts import render

from .models import Post, Tag

def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'mainApp/index.html', context={'posts': posts})

def post_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'mainApp/post_detail.html', context={'post': post})

def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'mainApp/tags_list.html', context={'tags': tags})