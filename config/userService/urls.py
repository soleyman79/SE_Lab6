from django.urls import path

from .views import ProfileListCreateView


urlpatterns = [
    path('profile', ProfileListCreateView.as_view())
]
