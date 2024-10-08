from rest_framework import serializers
from .models import Hospital, CustomUser, UserType
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address']


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(read_only=True)
    user_type = UserTypeSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'hospital', 'user_type']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT Serializer to add additional data (user_type, hospital)
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims (additional data to the token)
        token['hospital'] = user.hospital.name
        token['user_type'] = user.user_type.name

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Include the additional info in the response body
        data['hospital'] = self.user.hospital.name
        data['user_type'] = self.user.user_type.name

        return data

