
'''
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q 
from django.contrib.auth.hashers import check_password


User=get_user_model()

class EmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            admin=User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
        except User.DoesNotExist:
            return None
        if admin and check_password(admin, admin.password):
            return admin

        return None

'''

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import check_password




User=get_user_model()

class EmailPhoneUsernameAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user=User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
        except User.DoesNotExist:
           
            return  None
        if user and check_password(user, user.password):
            return user
       
        else:
            return None