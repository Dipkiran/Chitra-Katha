from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from datetime import timezone

#user table
class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE,)

#mainimage
class MainImage(models.Model):
    place = models.CharField(max_length=120)
    shortdescription = models.CharField(max_length=80)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.FileField()
    published_Date = models.DateTimeField(auto_now=False, auto_now_add=True)

#image table
class AddImage(models.Model):
    place = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    mainimage = models.FileField()
    published_Date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse("chitrakatha:imagelist", kwargs={"id":self.id})

    def get_url(self):
        return reverse("chitrakatha:imagelist", kwargs={"id":self.id})

#name of imagefilename
def get_image_filename(instance, filename):
    title = instance.post.place
    return "%s/%s" % (title, filename)

#multiple images linked to above addimage table
class Images(models.Model):
    post = models.ForeignKey(AddImage, default=None,on_delete=models.CASCADE,)
    image = models.FileField(upload_to=get_image_filename, verbose_name='Image', blank=True,)

#caption of image images
class ImageCaption(models.Model):
    postimage = models.ForeignKey(Images, default=None,on_delete=models.CASCADE,)
    image_caption = models.TextField()

    def get_url(self):
        return reverse("chitrakatha:imagedetail", kwargs={"id":self.id})

#Buyers table
class Buyers(models.Model):
    Name = models.CharField(max_length=120)
    Phone = models.CharField(max_length=10)
    image_id = models.FileField()

    def get_absolute_url(self):
        return reverse("chitrakatha:thankyou")

#blog table
class Blog(models.Model):
    place = models.CharField(max_length=120)
    Description = models.TextField()
    mainimage = models.FileField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    published_Date = models.DateTimeField(auto_now=False, auto_now_add=True)


    def get_url(self):
        return reverse("chitrakatha:bloglist", kwargs={"id":self.id})

#multiple images list to above blog table
class BlogImages(models.Model):
    post = models.ForeignKey(Blog, default=None,on_delete=models.CASCADE,)
    image = models.FileField(upload_to=get_image_filename, verbose_name='Image', blank=True,)

#captions of blog images
class Caption(models.Model):
    post = models.ForeignKey(BlogImages, default=None,on_delete=models.CASCADE,)
    image_caption = models.TextField()


    def get_url(self):
        return reverse("chitrakatha:blogdetail", kwargs={"id":self.id})
