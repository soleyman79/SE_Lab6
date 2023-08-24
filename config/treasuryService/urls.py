from django.urls import path

from .views import BookCreateView, BookReadView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('create', BookCreateView.as_view()),
    path('read/<str:title>', BookReadView.as_view()),
    path('update/<str:title>', BookUpdateView.as_view()),
    path('delete/<str:title>', BookDeleteView.as_view()),
]
