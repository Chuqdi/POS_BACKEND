from users.serializers import SignUpSerializer,LoginUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import authentication
from drf_yasg.utils import swagger_auto_schema



class RegisterUserView(APIView):
    @swagger_auto_schema(
            query_serializer = SignUpSerializer,
            responses={
                '201': SignUpSerializer,
            },
            operation_id='SignUp Endpoint',
            operation_description='This API logs registers a user.'
    )
    def post(self, request):
        s = SignUpSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(
                data ={
                    "user":s.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            s.errors
        )


class LoginUserView(APIView):
    @swagger_auto_schema(
            query_serializer = LoginUserSerializer,
            responses={
                '201': LoginUserSerializer,
            },
            operation_id='Login Endpoint',
            operation_description='This API logs users in. It takes the users email and password and return a token'
    )
    def post(self, request):
        user = authenticate(
            email=request.data.get("email"),
            password = request.data.get("password")
        )
        
        if user is not None:
            return Response(
                data={
                    "user":SignUpSerializer(user).data,
                    "token":user.auth_token.key
                }
            )
        return Response(
            data={
                "message":"User Credentials are not correct",
            },
            status=status.HTTP_404_NOT_FOUND
        )
