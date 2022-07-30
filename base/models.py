from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django.core.validators import email_re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class Member(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # title = models.CharField(max_length=200)
    # description = models.TextField(null=True, blank=True)
    # complete = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(
        max_length=200, null=False, default='')
    last_name = models.CharField(
        max_length=200, null=False, default='')
    email = models.EmailField(
        max_length=70, null=True, blank=True, unique=True)
    #phone = PhoneNumberField(null=False, blank=False,unique = False, default = 'NA')
    phone = PhoneNumberField(default='')

    Reg = 'Regular'
    Admin = 'Admin'

    Role_options = (
        (Reg, "Regular - Can't delete members"),
        (Admin, "Admin - Can delete memebers")
    )
    role = models.CharField(max_length=10, choices=Role_options, default=Reg)

    def save(self, *args, **kwargs):
        # ... other things not important here
        self.email = self.email.lower().strip()  # Hopefully reduces junk to ""

        try:
            validate_email(self.email)
        except ValidationError as ex:
            return False
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name
