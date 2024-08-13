from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        create a new user using the given fields
        """
        if not email:
            raise ValueError("Please provide a valid email address")
    
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create super user using the fields and email and password
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super user must have is staff is True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super user must have is superuser is True"))
 
        return self.create_user(email=email, password=password, **extra_fields)
        
        




