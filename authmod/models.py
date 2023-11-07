from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class NewUserManager(UserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email) 
        user = self.model(email=email) 
        user.set_password(password)
        user.save(using=self.db)
        return user

class User(AbstractUser):
    objects = NewUserManager()
    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    email_verified = models.BooleanField(default=False)
    mech = models.BooleanField(default=False) #True if mech, False if user