from django.urls import path
from .views import Home,About,Contact,FAQS,Blogs,Service,PersonalBrand,imageconsulting,corporaterebranding,\
                   Blogdetails,service_home,launchpad,Policy,Questionsform,Works,Tdh,Carrers

urlpatterns = [
    path('', Home , name='home'),
    path('ourstory/', About , name='ourstory'),
    path('faqs/', FAQS , name='faqs'),
    path('reach-us-out/', Contact , name='reach-us-out'),
    path('expertise/', service_home , name='expertise'),
    path('ideas/', Blogs , name='ideas'),
    path('brandconsulting/', Service , name='brandconsulting'),
    path('personalbrand/', PersonalBrand , name='personalbrand'),
    path('imageconsulting/', imageconsulting , name='imageconsulting'),
    path('launchpad/', launchpad , name='launchpad'),
    path('corporaterebranding/', corporaterebranding , name='corporaterebranding'),
    path('blog/<str:slug>', Blogdetails , name='blog'),
    path('questions/', Questionsform , name='questions'),
    path('privacy-policy/', Policy , name='privacy-policy'),
    path('works/', Works , name='works'),
    path('tenali-double-horse/', Tdh , name='tenali-double-horse'),
    path('carrerspage/', Carrers , name='carrerspage'),
   
    
]