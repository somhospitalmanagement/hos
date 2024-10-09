# Super/account/serializers.py

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'hospital', 'department', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        if 'hospital' not in validated_data or 'department' not in validated_data or 'user_type' not in validated_data:
            raise serializers.ValidationError("Hospital, department, and user type must be provided.")

        
        user = CustomUser(**validated_data)
        
        
        user.set_password(validated_data['password'])
        
        
        user.save()
        
        return user
    

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is associated with this email address.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = CustomUser.objects.get(email=email)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        send_mail(
            'Password Reset Request',
            f'Use the link to reset your password: {settings.FRONTEND_URL}/reset-password/{uid}/{token}/',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField()
    uid = serializers.CharField()

    def validate(self, attrs):
        try:
            uid = urlsafe_base64_decode(attrs['uid']).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, attrs['token']):
            return attrs
        raise serializers.ValidationError("Invalid token or user ID.")

    def save(self):
        user = CustomUser.objects.get(pk=urlsafe_base64_decode(self.validated_data['uid']).decode())
        user.set_password(self.validated_data['password'])
        user.save()