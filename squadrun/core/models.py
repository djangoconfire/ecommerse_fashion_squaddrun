from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from crum import get_current_user
from django.utils.translation import pgettext_lazy


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False,is_active=True, **extra_fields):
        'Creates a User with the given username, email and password'
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=is_active,
                          is_staff=is_staff, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True,
                                is_superuser=True, **extra_fields)


@python_2_unicode_compatible
class User(PermissionsMixin, AbstractBaseUser):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    gcm = models.CharField(max_length=150, null=False)
    email = models.EmailField(unique=True, null=True)
    mobile = models.BigIntegerField(unique=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    picture = models.CharField(max_length=1024, blank=True, null=True)
    thumbnail = models.CharField(max_length=1024, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    referral_code = models.CharField(max_length=15, blank=True, null=True)
    is_staff = models.BooleanField(
        pgettext_lazy('User field', 'staff status'),
        default=False)
    is_player = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)
    is_active = models.BooleanField(
        pgettext_lazy('User field', 'active'),
        default=False)
    date_joined = models.DateTimeField(
        pgettext_lazy('User field', 'date joined'),
        default=timezone.now, editable=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.email

    def get_username(self):
        """Return the identifying username for this User"""
        return self.email


class BaseModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', default=get_current_user())
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+', null=True, default=get_current_user)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True