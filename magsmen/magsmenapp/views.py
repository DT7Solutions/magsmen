from django.shortcuts import render
from .models import BlogPost
# Create your views here.
def Home(request):
    blog_list = BlogPost.objects.filter().order_by('-Id')[:3]     #filter(status=1).order_by('Create_at')
    return render(request, 'uifiles/home.html',{'blog_list':blog_list})

def About(request):
    return render(request, 'uifiles/about.html')

def FAQS(request):
    return render(request, 'uifiles/faqs.html')

def Contact(request):
    return render(request, 'uifiles/contact.html')

def Blogs(request):
    blog = BlogPost.objects.filter().order_by('-Id')
    return render(request, 'uifiles/blogs.html',{'blog':blog})

def Service(request):
    return render(request, 'uifiles/brandconsulting.html')

def PersonalBrand(request):
    return render(request, 'uifiles/personalbranding.html')

def imageconsulting(request):
    return render(request, 'uifiles/imageconsulting.html')

def corporaterebranding(request):
    return render(request, 'uifiles/corporaterebranding.html')



def Blogdetails(request,id):
    selectpost = BlogPost.objects.get(Id=id)
    return render(request, 'uifiles/blog-details.html',{'selectpost':selectpost})
