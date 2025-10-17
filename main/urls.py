from django.urls import path 
from .views import ProfileApiView
urlpatterns = [
    path('me/', ProfileApiView.as_view())
]