from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit = models.IntegerField(null=False, default=0)
    totalLoan = models.SmallIntegerField(null=False, default=0)

    def addCredit(self, amount):
        self.credit += amount

    def addLoan(self):
        self.totalLoan += 1

    def __str__(self) -> str:
        return f'{self.user.username}'
