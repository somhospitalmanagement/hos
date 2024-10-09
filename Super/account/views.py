# Super/account/views.py

# Super/account/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser
from .serializers import (
    CustomUserSerializer,
    CustomTokenObtainPairSerializer,
    PasswordResetRequestSerializer,
    PasswordResetSerializer
)
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import logging

# Set up logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
def admin_login(request):
    """
    Admin login to manage hospital settings.
    """
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        logger.info(f"Admin login successful for user: {serializer.validated_data['username']}")
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
    logger.warning(f"Admin login failed for user: {request.data.get('username')}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_user(request):
    """
    Admin creates a new user account (nurse, pharmacist, lab technician, etc.).
    """
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        logger.info(f"User created: {user.username}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    logger.warning(f"User creation failed: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    """
    User login to access department-specific functionalities.
    """
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        logger.info(f"User login successful for user: {serializer.validated_data['username']}")
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
    logger.warning(f"User login failed for user: {request.data.get('username')}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """
    Log out a user and invalidate the JWT token.
    """
    refresh_token = request.data.get("refresh")
    if refresh_token:
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"User logged out successfully: {request.user.username}")
            return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger.error(f"Error logging out user: {str(e)}")
            return Response({"error": "An error occurred while logging out."}, status=status.HTTP_400_BAD_REQUEST)
    
    logger.warning("Logout attempt without refresh token.")
    return Response({"error": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def password_reset_request(request):
    """
    Request a password reset link.
    """
    serializer = PasswordResetRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Password reset link sent to: {serializer.validated_data['email']}")
        return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)
    
    logger.warning(f"Password reset request failed: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def password_reset(request):
    """
    Reset the user's password.
    """
    serializer = PasswordResetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Password has been reset successfully for user ID: {serializer.validated_data['uid']}")
        return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
    
    logger.warning(f"Password reset failed: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_users_by_role(request):
    """
    List users filtered by their role.
    """
    user_type = request.query_params.get('user_type', None)
    if user_type:
        users = CustomUser.objects.filter(user_type=user_type)
    else:
        users = CustomUser.objects.all()

    serializer = CustomUserSerializer(users, many=True)
    logger.info(f"Listed users by role: {user_type if user_type else 'all users'}")
    return Response(serializer.data, status=status.HTTP_200_OK)