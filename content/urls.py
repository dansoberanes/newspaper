from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^articles/', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
]