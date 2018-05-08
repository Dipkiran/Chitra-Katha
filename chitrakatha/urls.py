from django.conf.urls import url
from django.contrib import admin

from . import views

app_name='chitrakatha'

urlpatterns = [
    url(r'^$', views.userpage, name='index'),
    url(r'^adminpage/$', views.adminpage, name='adminpage'),
    #upload pages
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^upload/image$', views.image, name='image'),
    url(r'^upload/blog$', views.blog, name='blog'),

    #images pages
    url(r'^images/$', views.images, name='images'),
    url(r'^images/(?P<id>\d+)/$', views.image_list, name='imagelist'),
    url(r'^images/(?P<id>\d+)/detail$', views.imagedetail, name='imagedetail'),

    #blog pages
    url(r'^blogs/$', views.blogs, name='blogs'),
    url(r'^blogs/(?P<id>\d+)/$', views.blog_list, name='bloglist'),
    url(r'^blogs/(?P<id>\d+)/detail$', views.blogdetail, name='blogdetail'),

    #login pages
    url(r'^login',views.sign_in.as_view(), name= 'login'),
    url(r'^logout',views.sign_out, name= 'logout'),

    #aboutpages
    url(r'^aboutme/$', views.aboutme, name='aboutme'),

    url(r'^adminpage/postview$', views.viewpage, name='viewpage'),

    #delete
    # url(r'^adminpage/imageview$', views.viewpage, name='viewpage'),

    # url(r'^adminpage/postview/(?P<id>\d+)/$', views.blogdelete, name='blogupdate'),


]
