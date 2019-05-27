from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
'''
제네릭 뷰
뷰 개발 과정에서 공통적으로 사용할 수 있는 기능들을 추상화하고,
장고에서 기본적으로 제공해주는 클래스형 뷰
https://docs.djangoproject.com/ko/2.2/ref/class-based-views/
'''

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'