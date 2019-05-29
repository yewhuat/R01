from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404


from .models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile

#    def get_object(self):
#        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        return context
