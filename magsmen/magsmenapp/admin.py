from django.contrib import admin
from .models import BlogPost,Category,ContactData,Media,StepformData
# Register your models here.


class AdminHappyCategories(admin.ModelAdmin):
    list_display=('Name','Created')


class AdminHappyBlogpost(admin.ModelAdmin):
    list_display=('Id','Category','Title','Tags','CreatedName','Create_at','status')
    list_filter = ["CreatedName",'Create_at']

class AdminMedia(admin.ModelAdmin):
    list_display = ['Title','Image','Slug']


class AdminHappyContact(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Subject','Message')



class AdminStepformData(admin.ModelAdmin):
    list_display = ['Name','Email','Phone','Brandmarketposition','BrandCorevalue','Brandperceive_targetaudience','CustomerFeedback','BrandPerformence','Challenges_Obstacles']


admin.site.register(Category,AdminHappyCategories)
admin.site.register(BlogPost,AdminHappyBlogpost)
admin.site.register(Media,AdminMedia)
admin.site.register(ContactData,AdminHappyContact)
admin.site.register(StepformData,AdminStepformData)
