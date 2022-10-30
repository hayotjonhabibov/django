from django.urls import path
from.views import HomePageView, AboutPageView, HelpPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('help/', HelpPageView.as_view(), name='help'),
    path('',HomePageView.as_view(), name='home'),
]
