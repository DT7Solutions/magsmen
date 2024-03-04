from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from .models import BlogPost,ContactData
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages
from django.http import HttpResponse
import requests


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os 

# Create your views here.
def Home(request):
    blog_list = BlogPost.objects.filter().order_by('-Id')[:3]     #filter(status=1).order_by('Create_at')
    return render(request, 'uifiles/home.html',{'blog_list':blog_list})

def About(request):
    return render(request, 'uifiles/about.html')

def FAQS(request):
    return render(request, 'uifiles/faqs.html')


def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        oContactinfo = ContactData(Email=email,Phone=phone,Subject=subject,Message=message)
        oContactinfo.save()
        
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['connect@magsmen.in']) 
            messages.success(request,'Message has been sucesfully send')
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')
    return render(request, 'uifiles/contact.html')

def Blogs(request):
    blog = BlogPost.objects.filter().order_by('-Id')
    # allposts = BlogPost.objects.all()
    paginator = Paginator(blog, 9) # paginate 10 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'uifiles/blogs.html',{'blog':posts,'posts':posts,'page':page})

def Service(request):
    return render(request, 'uifiles/brandconsulting.html')

def PersonalBrand(request):
    return render(request, 'uifiles/personalbranding.html')

def imageconsulting(request):
    return render(request, 'uifiles/imageconsulting.html')

def corporaterebranding(request):
    return render(request, 'uifiles/corporaterebranding.html')

def service_home(request):
    return render(request, 'uifiles/service.html')

def launchpad(request):
    return render(request, 'uifiles/launchpad.html')


def Blogdetails(request,slug):
    selectpost = BlogPost.objects.get(Sluglink=slug)
    return render(request, 'uifiles/blog-details.html',{'selectpost':selectpost})



def Questionsform(request):
    return render(request, 'uifiles/multistepform.html')

def Policy(request):
    return render(request,'uifiles/privacy-policy.html')

def Works(request):
    return render(request,'uifiles/works.html')
def Tdh(request):
    return render(request,'uifiles/tdh.html')
def Carrers(request):
    return render(request,'uifiles/carrers.html')

def Newsletter(request):
   
    pdf_filename = 'news-letter-august-2023.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename}"'
    return response
def Newslettertwo(request):
   
    pdf_filename_two = 'the-name-of-the-article-indian-brand-success-stories.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_two)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_two}"'
    return response
# def Newsletterthree(request):
   
#     pdf_filename_two = 'brand-corner-november-edition.pdf'
#     pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_two)
    
#     response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="{pdf_filename_two}"'
#     return response

def Newsletterthree(request):
    pdf_url = 'https://krysta-asset.s3.ap-south-1.amazonaws.com/Papers/aadhar.jpg'

    # Fetch the image content from the URL
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {e}', status=500)

    # Set the Content-Type header based on the image type
    content_type = response.headers.get('Content-Type', 'image/jpeg')

    # Set the Content-Disposition header to force download
    filename = pdf_url.split('/')[-1]
    response = HttpResponse(response.content, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response