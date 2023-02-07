from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'uifiles/home.html')

def About(request):
    return render(request, 'uifiles/about.html')

def FAQS(request):
    return render(request, 'uifiles/faqs.html')

def Contact(request):
    return render(request, 'uifiles/contact.html')

def Blogs(request):
    return render(request, 'uifiles/blogs.html')

def Service(request):
    return render(request, 'uifiles/brandconsulting.html')

def PersonalBrand(request):
    return render(request, 'uifiles/personalbranding.html')

def imageconsulting(request):
    return render(request, 'uifiles/imageconsulting.html')

def corporaterebranding(request):
    return render(request, 'uifiles/corporaterebranding.html')



def Casestudy(request):
    return render(request, 'uifiles/service1.html')