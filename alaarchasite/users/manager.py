from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.phonenumber import PhoneNumber
from email_validator import validate_email
from phonenumbers import parse
from alaarchasite.settings import PHONENUMBER_DEFAULT_REGION

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        elif not validate_email(email).email:
            raise ValueError('The email must exists')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        phone_number = parse(extra_fields.get('phone_number'), region=PHONENUMBER_DEFAULT_REGION)
        print(phone_number)
        if not PhoneNumber.is_valid(phone_number):
            raise ValueError('Phone number invalid')
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
