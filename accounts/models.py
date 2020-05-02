from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, commit=True):
        """
        Create and saves a User with the given email, full name and password
        :param email:
        :param full_name:
        :param password:
        :param commit:
        :return:
        """
        if not email:
            raise ValueError("User must have email")
        if not full_name:
            raise ValueError("User must have full name")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        """
        Creates and saves a superuser with the given email, full name and password
        :param email:
        :param full_name:
        :param password:
        :return:
        """
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            commit=False
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return True


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    # password field is made available by AbstractBaseUser
    # last login field also made available by AbstractBaseUser
    full_name = models.CharField(_('full name'), max_length=100, blank=True)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether the user is treated as active or not. '
            'This is unselected in the case of a delete operation'
        ),
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into the admin site or not'
        ),
    )

    # is_superuser field made available by the PermissionsMixin
    # groups field made available by the PermissionMixin
    groups = []
    user_permissions = []
    # user_permissions also made available by the PermissionMixin

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return "{} <{}>".format(self.full_name, self.email)

    def has_perms(self, perm_list, obj=None):
        """
        Does the user have a specific permission?
        Always yes
        :param perm_list:
        :param obj:
        :return:
        """
        return True

    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the `app label`?
        Always Yes
        :param app_label:
        :return:
        """
        return True