from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "landing/base.html"


class ContactusView(TemplateView):
    template_name = "landing/contact_us.html"


class AboutView(TemplateView):
    template_name = "landing/about_us.html"
