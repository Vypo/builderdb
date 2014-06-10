from django.shortcuts import render
from django.views.generic import TemplateView

class SettingsView(TemplateView):
    template_name = 'accounts/settings.html'
