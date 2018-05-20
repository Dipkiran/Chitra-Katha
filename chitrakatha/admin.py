from django.contrib import admin

# Register your models here.
from .models import *
#model admin options
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","place","mainimage","published_Date",]
    #list_display_links = ["updated"]


    class Meta:
        model = AddImage
admin.site.register(AddImage, PostModelAdmin)

class MainImageModelAdmin(admin.ModelAdmin):
    list_display = ["id","place","shortdescription","image","published_Date",]
    #list_display_links = ["updated"]


    class Meta:
        model = MainImage
admin.site.register(MainImage, MainImageModelAdmin)

class ImageModelAdmin(admin.ModelAdmin):
    list_display = ["image","post","id",]
    #list_display_links = ["updated"]


    class Meta:
        model = Images
admin.site.register(Images, ImageModelAdmin)

class BuyerModelAdmin(admin.ModelAdmin):
    list_display = ["id","Name","Phone","image_id",]
    #list_display_links = ["image_id"]


    class Meta:
        model = Buyers
admin.site.register(Buyers, BuyerModelAdmin)
class BlogImagesModelAdmin(admin.ModelAdmin):
    list_display = ["image","post","id",]
    #list_display_links = ["updated"]


    class Meta:
        model = BlogImages
admin.site.register(BlogImages, BlogImagesModelAdmin)

class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['place', 'Description','mainimage','id', ]
    #list_display_links = ["updated"]


    class Meta:
        model = Blog
admin.site.register(Blog, BlogModelAdmin)

class CaptionModelAdmin(admin.ModelAdmin):
    list_display = ['post', 'image_caption','id', ]
    list_display_links = ["id"]


    class Meta:
        model = Caption
admin.site.register(Caption, CaptionModelAdmin)

class ImageCaptionModelAdmin(admin.ModelAdmin):
    list_display = ['postimage', 'image_caption','id', ]
    list_display_links = ["id"]


    class Meta:
        model = ImageCaption
admin.site.register(ImageCaption, ImageCaptionModelAdmin)
