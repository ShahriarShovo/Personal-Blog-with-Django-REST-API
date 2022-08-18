from dataclasses import field
from rest_framework import serializers
from account.models import User


class Login_Serializers(serializers.ModelSerializer):
    uep=serializers.CharField(max_length=100)
    class Meta:
        model=User
        fields=['uep','email','phone','username','password']
        