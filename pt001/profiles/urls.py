from django.conf.urls import url, include
from .views import ProfileDetailView

urlpatterns = [
    url(r'^accounts/profile/(?P<username>[-\w]+)/$', ProfileDetailView.as_view(), name="profile-detail"),
]