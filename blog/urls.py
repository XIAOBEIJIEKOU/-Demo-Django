from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^index/$', views.index),   # 可以带正则表达式
    url(r'^article/(?P<article_id>[0-9]+)/$', views.show_article, name='article_page'),
    url('edit/(?P<article_id>[0-9]+)/$', views.edit_article, name='edit_page'),
    url('edit_action/', views.edit_action, name='edit_action'),
]