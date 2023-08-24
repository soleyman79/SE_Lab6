from rest_framework import serializers

from .models import Loan
from userService.models import Profile
from treasuryService.models import Book


class LoanSerializer(serializers.ModelSerializer):
    borrower = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    
    class Meta:
        model = Loan
        fields = ['borrower', 'book', 'borrowDate']