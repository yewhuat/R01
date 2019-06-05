from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView
from django.shortcuts import get_object_or_404


from .forms import ProfileModelForm
from .models import Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileModelForm
    template_name = 'profile_details.html'
    queryset = Profile.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_details.html'
#    def get_object(self):
#        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        return context
