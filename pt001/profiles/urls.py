from django.conf.urls import url, include
from .views import ProfileView

urlpatterns = [
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile"),
]