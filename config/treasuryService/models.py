from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128, null=False)
    pageNumbers = models.SmallIntegerField(null=True)
    isAvailable = models.BooleanField(default=True)

    def borrow(self):
        if not self.isAvailable:
            raise Exception('The book is unavailable.')
        else:
            self.isAvailable = False

    def giveBack(self):
        self.isAvailable = True
