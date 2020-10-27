from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^posts/(?P<id>[0-9]+)$', views.show, name='show'),
    url(r'^posts/new/$', views.post_new, name='post_new'),
    url(r'^posts/supp/(?P<id>[0-9]+)$', views.post_supp, name='post_supp'),
 
    url(r'^posts/upd(?P<id>[0-9]+)$', views.post_upd, name='post_upd'),
    
]