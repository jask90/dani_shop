import json

from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from register_bot.models import Profile
from register_bot.serializers import RegisterUserSerializer
from register_bot.tasks import send_welcome_email


@swagger_auto_schema(methods=['post',], request_body=RegisterUserSerializer)
@api_view(['POST'])
@authentication_classes((BasicAuthentication, OAuth2Authentication,))
@permission_classes((IsAuthenticated,))
def register_user(request):
    """
    Register a User and send welcome email
    """
    response = {}
    profile = None

    serializer = RegisterUserSerializer(data=request.data)

    if serializer.is_valid():
        with transaction.atomic():
            data = serializer.validated_data
            user, created = User.objects.get_or_create(username=data['email'], email=data['email'], first_name=data['name'])
            profile, created = Profile.objects.get_or_create(user=user, phone=data['phone'], country=data['country'])
    else:
        response['errors'] = serializer.errors
        return HttpResponse(json.dumps(response), status=status.HTTP_400_BAD_REQUEST)

    if profile:
        # After 1 min, we are going to send a welcome email
        send_welcome_email.s(profile.user.email).apply_async(countdown=60)
    else:
        response['errors'] = 'Something was wrong with User registrations'
        return HttpResponse(json.dumps(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)
