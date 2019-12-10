from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import UserProfile
from .serializers import UserProfileSerializer
from user import permissions

###

from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import permissions as pm


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = (pm.AllowAny, )

    def post(self, request):
        user = request.data.get('user')
        if not user:
            return Response({'response': 'error', 'message': 'No data found'})
        serializer = UserSerializerWithToken(data=user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response": "error", "message": serializer.errors})
        return Response({"response": "success", "message": "user created succesfully"})

###


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


# class UserLoginApiView(ObtainAuthToken):
#     """Handle creating user authentication tokens"""
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
