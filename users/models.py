from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db.models.signals import post_save



class UserManager(BaseUserManager):
    def create(self, email, first_name,last_name, password):
        if  not email:
            raise ValueError("Please enter your  email")
        

        if  not first_name:
            raise ValueError("Please enter your first name")

        if  not last_name:
            raise ValueError("Please enter your  last name")

        if password:
            raise ValueError("Please enter your password")

        user  = self.model(
            last_name=last_name, 
            first_name = first_name,
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    

    def  create_super_user(self, email, first_name,last_name, password):
        user = self.create_user(email, first_name,last_name, password)
        user.is_active=True
        user.is_super=True
        user.is_staff = True
        user.is_admin=True
        user.save(using=self._db)
        return user




class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email  = models.EmailField(unique=True, blank=False, null=False, max_length=90)
    is_new = models.BooleanField(default=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]



    def perm(self, *args, **kwargs):
        return True
    
    def perm_module(self, *args, **kwargs):
        return True

def user_created(sender, instance, created, *rgs, **kwargs):
    pass

    

post_save.connect(user_created, sender=User)
