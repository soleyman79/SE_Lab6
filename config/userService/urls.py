from django.urls import path

from .views import ProfileCreateView, ProfileReadView, ProfileUpdateView, ProfileDeleteView


urlpatterns = [
    path('create', ProfileCreateView.as_view()),
    path('read/<str:username>', ProfileReadView.as_view()),
    path('update/<str:username>', ProfileUpdateView.as_view()),
    path('delete/<str:username>', ProfileDeleteView.as_view()),
]
