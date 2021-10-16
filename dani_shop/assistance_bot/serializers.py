from rest_framework import serializers
from django.contrib.auth.models import User
from assistance_bot.models import Topic


class TopicField(serializers.RelatedField):
    def get_queryset(self):
        return Topic.objects.all()

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            topic = Topic.objects.get(name=data)
        except:
            raise serializers.ValidationError(f'Topic not found {data}')
        return topic


class AskQuestionSerializer(serializers.Serializer):
    topic = TopicField(many=False, read_only=False, required=True)
    question = serializers.CharField()
    email = serializers.EmailField()
