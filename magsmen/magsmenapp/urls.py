from django.urls import path
from .views import Home,About,Contact,FAQS,Blogs,Service,Casestudy,PersonalBrand,imageconsulting,corporaterebranding
urlpatterns = [
    path('', Home , name='home'),
    path('about/', About , name='about'),
    path('faqs/', FAQS , name='faqs'),
    path('contact/', Contact , name='contact'),
    path('blogs/', Blogs , name='blogs'),
    path('brandconsulting/', Service , name='brandconsulting'),
    path('personalbrand/', PersonalBrand , name='personalbrand'),
    path('imageconsulting/', imageconsulting , name='imageconsulting'),
    path('corporaterebranding/', corporaterebranding , name='corporaterebranding'),
    path('casestudy/', Casestudy , name='casestudy'),
]