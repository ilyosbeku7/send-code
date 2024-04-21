from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from .manager import Usermanager
# Create your models here.


class User(AbstractBaseUser):
    phone_number=models.CharField(max_length=13, unique=True)
    is_phone_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=5)

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    # objects=Usemanager