from django.db import models
import random
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

    def generate_otp(self):
        otp = random.randint(1000, 9999)
        self.otp = otp

    def save(self, *args, **kwargs):
        if not self.otp:
            self.generate_otp()
        super().save(*args, **kwargs)