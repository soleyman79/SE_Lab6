from django.urls import path

from .views import *


urlpatterns = [
    path('create', LoanCreateView.as_view()),
    path('read_book/<str:book__title>', LoanReadByBookView.as_view()),
    path('read_user/<str:borrower__username>', LoanReadByUserView.as_view()),
    path('update_book/<str:book__title>', LoanUpdateByBookView.as_view()),
    path('update_user/<str:borrower__username>', LoanUpdateByUserView.as_view()),
    path('delete/<str:book__title>', LoanDeleteView.as_view()),
]
