from datetime import date
import json
from xml.dom.minidom import Document
from django.conf import settings
from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from .models import BlogPost,ContactData,Media,StepformData
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages




from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os 

# Create your views here.
def Home(request):
    blog_list = BlogPost.objects.filter().order_by('-Id')[:2]     #filter(status=1).order_by('Create_at')


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
def Triplex(request):
    return render(request, 'uifiles/triplex.html')

def Zavaine(request):
    return render(request, 'uifiles/zavaine.html')
def Rishikatdh(request):
    return render(request, 'uifiles/rishikatdh.html')

def Vsb(request):
    return render(request, 'uifiles/vsb.html')

def imageconsulting(request):
    return render(request, 'uifiles/imageconsulting.html')

def corporaterebranding(request):
    return render(request, 'uifiles/corporaterebranding.html')

def service_home(request):
    return render(request, 'uifiles/service.html')

def launchpad(request):
    return render(request, 'uifiles/launchpad.html')

def brandexpresso(request):
    return render(request, 'uifiles/brandexpresso.html')

def brandcreation(request):
    return render(request, 'uifiles/brandcreation.html')


def Blogdetails(request,slug):
    selectpost = BlogPost.objects.get(Sluglink=slug)
    return render(request, 'uifiles/blog-details.html',{'selectpost':selectpost})


def Questionsform(request):
    if request.method == 'POST':
        storedFormData = request.POST.get('storedFormData')
        
        # Convert JSON string to dictionary
        stored_form_data = json.loads(storedFormData)
        
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # phone=request.POST.get('phone')
        # storedFormData = request.POST.get('storedFormData')
        brandposition = request.POST.get('brandposition')
        corevalue = request.POST.get('corevalue')
        brandtarget = request.POST.get('brandtarget')
        customerfeedback = request.POST.get('customerfeedback')
        brandperform = request.POST.get('brandperform')
        brandchallenge = request.POST.get('brandchallenge')
        brandmotivation = request.POST.getlist('brandcheck')
        achieve = request.POST.get('achieve')
        brandexpectation = request.POST.get('brandexpectation')

        oQuestion_data = StepformData(Name=stored_form_data.get('name'),Email=stored_form_data.get('email'),Phone=stored_form_data.get('phone'),Brandmarketposition=brandposition,BrandCorevalue=corevalue,Brandperceive_targetaudience=brandtarget,CustomerFeedback=customerfeedback,BrandPerformence=brandperform,Challenges_Obstacles=brandchallenge,Brand_Motivation=brandmotivation,Goals_Achieves=achieve,Expectations=brandexpectation)
        oQuestion_data.save()
        
         # Send email notification
        subject = 'Form Submission Notification'
        message = 'A form has been submitted with the following details:\n\n' \
                  f'Name: {stored_form_data.get("name")}\n' \
                  f'Email: {stored_form_data.get("email")}\n' \
                  f'Phone: {stored_form_data.get("phone")}\n\n' \
                  'Additional form details:\n' \
                  f'Brand Position: {brandposition}\n' \
                  f'Core Value: {corevalue}\n' \
                  f'Target Audience: {brandtarget}\n' \
                  f'Customer Feedback: {customerfeedback}\n' \
                  f'Brand Performance: {brandperform}\n' \
                  f'Brand Challenge: {brandchallenge}\n' \
                  f'Brand Motivation: {", ".join(brandmotivation)}\n' \
                  f'Achievements: {achieve}\n' \
                  f'Brand Expectation: {brandexpectation}'
        
        from_email = 'connectmagsmen@gmail.com'  # Update with your sender email
        to_email = ['connect@magsmen.in']  # Update with recipient email(s)
        
        try:
            send_mail(subject, message,'connectmagsmen@gmail.com', recipient_list=['connect@magsmen.in'])
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return render(request, 'uifiles/multistepform.html')



def Policy(request):
    return render(request,'uifiles/privacy-policy.html')

def Works(request):
    return render(request,'uifiles/works.html')
def Tdh(request):
    return render(request,'uifiles/tdh.html')
def Carrers(request):
    return render(request,'uifiles/carrers.html')
def Suryacolours(request):
    return render(request,'uifiles/suryaccolours.html')
def Tenalidoublehorse(request):
    return render(request,'uifiles/tenalidoublehorse.html')

def Ourmedia(request):
    media = Media.objects.filter().order_by('-Id')
    paginator = Paginator(media, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'uifiles/media.html',{'media':posts,'posts':posts,'page':page})


def error404(request,exception):
    return render(request, 'uifiles/404.html')




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
def Newsletterthree(request):
   
    pdf_filename_two = 'brand-corner-november-edition.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_two)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_two}"'
    return response

def Brand(request):
    pdf_filename_three = 'brand-architecture.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_three)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_three}"'
    return response


def BrandRefresh(request):
    pdf_filename_four = 'brand-refresh-rebranding-june.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_four)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_four}"'
    return response


def DigitalTwin_BrandStrategy(request):
    pdf_filename_five = 'digital-twin-brand-strategy.pdf'
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename_five)
    
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_filename_five}"'
    return response




# def Newsletterthree(request):
#     pdf_url = 'https://krysta-asset.s3.ap-south-1.amazonaws.com/Papers/aadhar.jpg'

#     try:
#         response = requests.get(pdf_url)
#         response.raise_for_status()  
#     except requests.RequestException as e:
#         return HttpResponse(f'Error fetching image: {e}', status=500)

#     content_type = response.headers.get('Content-Type', 'image/jpeg')

    
#     filename = pdf_url.split('/')[-1]
#     response = HttpResponse(response.content, content_type=content_type)
#     response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
#     return response