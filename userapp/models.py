from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, password, **other_fields)
    
    def create_user(self, email, first_name, password, **other_fields):

        if not email:
            raise ValueError('you must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
        
class MyUser(AbstractBaseUser, PermissionsMixin):
    # id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(null=True,  max_length=255)
    last_name = models.CharField(null=True,  max_length=255)
    email = models.EmailField('email address',unique = True, max_length=255)
    # password = models.TextField(unique=True)
    phone = models.BigIntegerField(null=True)
    skill_id = models.BigIntegerField(null=True)
    topic = models.TextField(null=True,  max_length=550)
    added_by = models.TextField(null=True)
    role_id = models.BigIntegerField(null=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    created_by = models.TextField(null=True)
    updated_by = models.TextField(null=True)
    feedback = models.TextField(null=True)
    result = models.TextField(null=True)
    admin_id = models.BigIntegerField(null=True)
    validation = models.BigIntegerField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


    class Meta:
        db_table = 'tbl_users'
