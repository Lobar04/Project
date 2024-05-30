from django.db import models

# Create your models here.
class ContactModel(models.Model):
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_message = models.CharField(max_length=1000)

    class Meta:
        db_table = 'contact'
        verbose_name_plural = 'Contacts'


class InfoForMainPage(models.Model):
    address = models.CharField(max_length=10000)
    telephone_number = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Information for main page'
        db_table = 'info'
