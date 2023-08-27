from rest_framework import serializers

import sys
import os

borrow_service_dir = os.path.abspath('../.')
sys.path.append(borrow_service_dir)

from .models import Loan
from userService.info.models import Profile
from treasuryService.book.models import Book


class LoanSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    
    class Meta:
        model = Loan
        fields = ['borrower', 'book', 'borrowDate']