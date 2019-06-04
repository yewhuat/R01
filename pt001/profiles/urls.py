from django.conf.urls import url, include
from .views import ProfileDetailView

urlpatterns = [
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile'),
]