
from django.urls import path, include
from .views import translationview

urlpatterns = [
    path('', translationview, name='siteview')
]
