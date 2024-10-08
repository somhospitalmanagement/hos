
from django.contrib.auth import get_user_model  # Import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Hospital  # Importing the Hospital model
from .serializers import CustomUserSerializer, HospitalSerializer, CustomTokenObtainPairSerializer

User = get_user_model()  # Get the currently active user model

@api_view(['POST'])
def hospital_login(request):
    """
    Hospital login to get JWT token.
    """
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users_by_role(request):
    """
    List users based on role for a specific hospital.
    """
    user_type = request.query_params.get('user_type')
    if user_type is None:
        return Response({"error": "user_type parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    users = User.objects.filter(  # Use User instead of CustomUser
        hospital=request.user.hospital,
        user_type__name=user_type
    )
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hospital_detail(request, pk):
    """
    Retrieve details of a specific hospital.
    """
    try:
        hospital = Hospital.objects.get(pk=pk)
        serializer = HospitalSerializer(hospital)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Hospital.DoesNotExist:
        return Response({"error": "Hospital not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """
    Log out a user and invalidate the JWT token.
    """
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


