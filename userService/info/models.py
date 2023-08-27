from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=128, primary_key=True, default=None)
    credit = models.IntegerField(null=False, default=0)
    totalLoan = models.SmallIntegerField(null=False, default=0)

    def addCredit(self, amount):
        self.credit += amount

    def addLoan(self):
        self.totalLoan += 1

    def __str__(self) -> str:
        return f'username: {self.username} credit: {self.credit} totalLoan: {self.totalLoan}'
