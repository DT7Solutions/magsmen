from django.contrib import admin
from .models import BlogPost,Category
# Register your models here.


class AdminHappyCategories(admin.ModelAdmin):
    list_display=('Name','Created')


class AdminHappyBlogpost(admin.ModelAdmin):
    list_display=('Id','Category','Title','Tags','CreatedName','Create_at','status')
    list_filter = ["CreatedName",'Create_at']


admin.site.register(Category,AdminHappyCategories)
admin.site.register(BlogPost,AdminHappyBlogpost)