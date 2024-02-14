from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.subject + '--Email:--' + self.Email
