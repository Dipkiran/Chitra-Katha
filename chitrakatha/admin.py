from django.contrib import admin

# Register your models here.
from .models import AddImage
from .models import Images
from .models import BlogImages
from .models import Blog
from .models import Buyers
from .models import Caption
from .models import ImageCaption
#model admin options
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","place","content","mainimage","published_Date",]
    #list_display_links = ["updated"]


    class Meta:
        model = AddImage
admin.site.register(AddImage, PostModelAdmin)

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
