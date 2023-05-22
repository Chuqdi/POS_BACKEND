from users.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError





class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length =8)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name"
        ]
        

    
    def validate(self, attrs):
        if User.objects.filter(email=attrs.get("email")).exists():
            raise ValidationError("User email already taken")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user




class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
           
        ]

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = User.objects.filter(email=email)
        if not user.exists():
            raise ValidationError("User with this Email does not exist")
        
        user = user[0]
        if not user.check_password(password, user.password):
            raise ValidationError("User password validation has failed")



        return attrs
    


