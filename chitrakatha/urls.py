from django.conf.urls import url
from django.contrib import admin

from . import views

app_name='chitrakatha'

urlpatterns = [
    url(r'^$', views.userpage, name='index'),
    url(r'^chitrakatha/$', views.mainpage, name='mainpage'),
    url(r'^chitrakatha/orders$', views.orders, name='orders'),
    #upload pages
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^upload/image$', views.image, name='image'),
    url(r'^upload/mainimage$', views.mainimage, name='mainimage'),
    url(r'^upload/blog$', views.blog, name='blog'),

    #images pages
    url(r'^images/$', views.images, name='images'),
    url(r'^images/(?P<id>\d+)/$', views.image_list, name='imagelist'),
    url(r'^images/(?P<id>\d+)/detail$', views.imagedetail, name='imagedetail'),
    url(r'^mainimage/(?P<id>\d+)/detail$', views.mainimagedetail, name='mainimagedetail'),

    #blog pages
    url(r'^blogs/$', views.blogs, name='blogs'),
    url(r'^blogs/(?P<id>\d+)/$', views.blog_list, name='bloglist'),
    url(r'^blogs/(?P<id>\d+)/detail$', views.blogdetail, name='blogdetail'),

    #login pages
    url(r'^login',views.sign_in.as_view(), name= 'login'),
    url(r'^logout',views.sign_out, name= 'logout'),

    #aboutpages
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^chitrakatha/postview$', views.viewpage, name='viewpage'),

    #delete
    url(r'^chitrakatha/images/(?P<id>\d+)$', views.deleteimage, name='deleteimage'),
    url(r'^chitrakatha/images/(?P<id>\d+)/delete$', views.imagedelete, name='imagedelete'),
    url(r'^chitrakatha/blog/(?P<id>\d+)$', views.deleteblog, name='deleteblog'),
    url(r'^chitrakatha/blog/(?P<id>\d+)/delete$', views.blogdelete, name='blogdelete'),


    #update
    url(r'^chitrakatha/blog/(?P<id>\d+)/update$', views.updateblog, name='updateblog'),

    # url(r'^adminpage/postview/(?P<id>\d+)/$', views.blogdelete, name='blogupdate'),

    url(r'^thankyou/$', views.thankyou, name='thankyou'),
]
