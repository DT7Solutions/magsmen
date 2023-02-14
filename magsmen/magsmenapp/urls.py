from django.urls import path
from .views import Home,About,Contact,FAQS,Blogs,Service,PersonalBrand,imageconsulting,corporaterebranding,Blogdetails,service_home
urlpatterns = [
    path('', Home , name='home'),
    path('about/', About , name='about'),
    path('faqs/', FAQS , name='faqs'),
    path('contact/', Contact , name='contact'),
    path('services/', service_home , name='services'),
    path('blogs/', Blogs , name='blogs'),
    path('brandconsulting/', Service , name='brandconsulting'),
    path('personalbrand/', PersonalBrand , name='personalbrand'),
    path('imageconsulting/', imageconsulting , name='imageconsulting'),
    path('corporaterebranding/', corporaterebranding , name='corporaterebranding'),
    path('blog/<str:slug>', Blogdetails , name='blog'),
]