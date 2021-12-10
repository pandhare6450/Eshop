from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

