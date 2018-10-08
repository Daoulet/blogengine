from django.urls import path
from django.views.generic import ListView, DetailView
from blog.models import Article

urlpatterns = [
    path('', ListView.as_view(queryset=Article.objects.all().order_by("-date"[:10]), template_name="blog/blog.html")),
    path('<int:pk>/', DetailView.as_view(model = Article, template_name = "blog/post.html")),
]


# url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date"), template_name="news/posts.html")),
# url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name = "news/post.html")),