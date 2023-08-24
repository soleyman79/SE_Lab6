from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128, primary_key=True)
    pagesNumber = models.SmallIntegerField(null=True)
    isAvailable = models.BooleanField(default=True)

    def borrow(self):
        if not self.isAvailable:
            raise Exception('The book is unavailable.')
        else:
            self.isAvailable = False

    def giveBack(self):
        self.isAvailable = True

    def __str__(self) -> str:
        return f'id: {self.pk} title: {self.title} pageNumbers: {self.pagesNumber} isAvailable: {self.isAvailable}'
