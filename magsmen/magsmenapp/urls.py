from django.urls import path
from .views import Home,About,Contact,FAQS,Blogs,Service,Casestudy,PersonalBrand
urlpatterns = [
    path('', Home , name='home'),
    path('about/', About , name='about'),
    path('faqs/', FAQS , name='faqs'),
    path('contact/', Contact , name='contact'),
    path('blogs/', Blogs , name='blogs'),
    path('brandconsulting/', Service , name='brandconsulting'),
    path('personalbrand/', PersonalBrand , name='personalbrand'),
    path('casestudy/', Casestudy , name='casestudy'),
]