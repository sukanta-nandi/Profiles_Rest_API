from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# create a profiles manager inheriting the base user model
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, email, name, password=None):
        """ Create a new user profile """

        if not email:
            raise ValueError('User Must have an email address')

        #normalize(lowercase) the second-half of email
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        #creates a hashed password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user"""
        # self is automatically passed from a class function
        user = self.create_user(email, name, password)

        #is_superuser automatically created by permissions mixin in userprofiles
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    #creating oblects from UserProfileManager
    objects = UserProfileManager()

    #overwriting default username field -> username using email
    USERNAME_FIELD = 'email'
    #additional required fileds(username is required by default)
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of model"""
        return self.email

    
        