from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email is not provided')

        NE=self.normalize_email(email)#NE---NORMALIZED_EMAIL

        UPO=self.model(email=NE,first_name=first_name,last_name=last_name)#self.model stores UserProfile class adress

        UPO.set_password(password)
        UPO.save()
        return UPO

    def create_superuser(self,email,first_name,last_name,password):
        UPO=self.create_user(email,first_name,last_name,password)
        UPO.is_staff=True
        UPO.is_superuser=True
        UPO.save()


class UserProfile(AbstractBaseUser,PermissionManager):
    email=models.EmailField(max_length=25,primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)

    is_admin=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=UserProfileManager()#objects is a special veriable of ABU

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
