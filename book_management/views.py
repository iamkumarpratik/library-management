from django.shortcuts import render
from django.http import JsonResponse
from .models import Members, Credentials
from .serializers import MembersSerializer, CredentialsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from bcrypt import hashpw, gensalt
# Create your views here.


@api_view(['GET'])
def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def signup(request):
    try:
        registration_data = request.data
        raw_password = registration_data['password'].encode('utf-8')
        password_salt = gensalt()
        hashed_password = hashpw(raw_password, password_salt)
        credentials_details = {'username': registration_data['username'], 'password': str(hashed_password)}
        members_details = {'username': registration_data['username'], 'fullname': registration_data['fullname'],
                           'email': registration_data['email'], 'active': True, 'role': 'member'}
        credentials_serializer = CredentialsSerializer(data=credentials_details)
        members_serializer = MembersSerializer(data=members_details)

        credentials_usernames = Credentials.objects.filter(username=registration_data['username']).only('username')
        list_users = []
        for users in credentials_usernames:
            list_users.append(users.username)

        if registration_data['username'] in list_users:
            raise Exception('User already exists!')

        response = None
        if credentials_serializer.is_valid() and members_serializer.is_valid():
            credentials_serializer.save()
            members_serializer.save()
            response = {
                "credentials": credentials_serializer.data['username'],
                "details": members_serializer.data,
            }
        if response is not None:
            return JsonResponse({"status": "success", "data": response}, status=status.HTTP_201_CREATED)
        else:
            raise Exception("Account registration failed.")

    except Exception as e:
        return JsonResponse({"status": "error", "message": f"{e}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)




