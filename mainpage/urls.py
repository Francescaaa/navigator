from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from mainpage.models import Post
from . import views
"""
urlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all() .order_by("-date")[:25],
                                            template_name="mainpage/mainpage.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                                            template_name = 'mainpage/post.html'))]
"""
urlpatterns = [
    url(r'^$',views.index),
    url(r'^updateURL/',views.scrape),
]
