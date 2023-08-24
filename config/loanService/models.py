from django.db import models

from config.treasuryService.models import Book
from config.userService.models import Profile


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Profile, on_delete=models.CASCADE)
    borrowDate = models.DateTimeField(auto_now_add=True)
    returnDate = models.DateTimeField(auto_now=True)
