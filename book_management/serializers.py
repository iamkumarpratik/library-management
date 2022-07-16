from rest_framework import serializers
from .models import Members, Credentials


class CredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credentials
        fields = ('username', 'password')


class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ('fullname', 'email', 'username', 'active', 'role')
