from rest_framework import generics

import sys
import os

borrow_service_dir = os.path.abspath('../.')
sys.path.append(borrow_service_dir)

from .models import Loan
from .serializers import LoanSerializer
from treasuryService.book.models import Book
from userService.info.models import Profile


class LoanCreateView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        data = self.request.data
        
        book = Book.objects.get(title=data['book'])
        book.borrow()
        book.save()

        borrower = Profile.objects.get(username=data['borrower'])
        borrower.addLoan()
        borrower.save()

        return super().perform_create(serializer)


class LoanReadByBookView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'book__title'


class LoanReadByUserView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'borrower__username'


class LoanUpdateByBookView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'book__title'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class LoanUpdateByUserView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'borrower__username'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class LoanDeleteView(generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'book__title'
    
    def delete(self, request, *args, **kwargs):
        book = Book.objects.get(title=kwargs['book__title'])
        book.giveBack()
        book.save()

        return super().delete(request, *args, **kwargs)