from django.conf.urls import url, include
from .views import ProfileDetailView, ProfileUpdateView

app_name = 'profile'

urlpatterns = [
    url(r'^profile/$', ProfileDetailView.as_view(), name='profile'),
    url(r'^profile/update/$', ProfileUpdateView.as_view(), name='profile_update'),
]