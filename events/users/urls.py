from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('events/', include('events_management.urls')),
    path('logout/', LogoutView.as_view(), name='logout')
]
