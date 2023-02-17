from django.contrib import admin
from .models import BlogPost,Category,ContactData
# Register your models here.


class AdminHappyCategories(admin.ModelAdmin):
    list_display=('Name','Created')


class AdminHappyBlogpost(admin.ModelAdmin):
    list_display=('Id','Category','Title','Tags','CreatedName','Create_at','status')
    list_filter = ["CreatedName",'Create_at']


class AdminHappyContact(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Subject','Message')

admin.site.register(Category,AdminHappyCategories)
admin.site.register(BlogPost,AdminHappyBlogpost)
admin.site.register(ContactData,AdminHappyContact)