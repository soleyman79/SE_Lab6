from django.db import models

import sys
import os

borrow_service_dir = os.path.abspath('../.')
sys.path.append(borrow_service_dir)

from treasuryService.book.models import Book
from userService.info.models import Profile


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True)
    borrower = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    borrowDate = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'book: {self.book.title} borrower: {self.borrower.username} borrowDate: {self.borrowDate}'
