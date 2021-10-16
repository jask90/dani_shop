import json

from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from assistance_bot.models import Channel, Topic
from assistance_bot.serializers import AskQuestionSerializer
from assistance_bot.tasks import *


@swagger_auto_schema(methods=['post',], request_body=AskQuestionSerializer)
@api_view(['POST'])
@authentication_classes((BasicAuthentication, OAuth2Authentication,))
@permission_classes((IsAuthenticated,))
def ask_question(request):
    """
    Send question to the related channels related to the Topic
    """
    response = {}

    serializer = AskQuestionSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data

        # We need to save possibles to call functions from strings
        possibles = globals().copy()
        topic = data['topic']

        for channel in topic.channels.all():
            try:
                possibles.get(channel.function).delay(data['question'], data['email'], topic.name)
            except:
                response['errors'] = f'Error with channel {channel.name}'
                return HttpResponse(json.dumps(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        response['errors'] = serializer.errors
        return HttpResponse(json.dumps(response), status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)
