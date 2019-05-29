from django.shortcuts import render
from django.views.generic import TemplateView


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/profile.html'

