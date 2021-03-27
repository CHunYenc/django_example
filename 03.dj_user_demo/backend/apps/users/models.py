from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager


# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email


class BaseUserManager(BaseUserManager):
    def create_user(self, email, company_name, phone, password=None):
        if not email:
            raise ValueError("email is required.")
        if not company_name:
            raise ValueError("company_name is required.")
        if not phone:
            raise ValueError("please provide an active phone number.")

        user = self.model(
            email=self.normalize_email(email),
            company_name=company_name,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, company_name, phone, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            company_name=company_name,
            phone=phone,
            password=password
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class BaseUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email_address", max_length=100, unique=True)
    company_name = models.CharField(verbose_name="company_name", max_length=200, unique=True)
    phone = models.CharField(verbose_name="company_phone", max_length=20)
    created_time = models.DateTimeField(verbose_name="created_time", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["company_name", "phone"]
    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
