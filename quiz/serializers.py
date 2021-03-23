
from rest_framework import serializers
from .models import Answer, Question, Poll, Choice


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('pk', 'choice_pk', 'choice_text', 'anon_id', 'question')


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['pk', 'text']


class ChoicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['pk', 'text', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )

    class Meta:
        model = Question
        fields = ['pk', 'text', 'choices']


class PollCreateSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField()

    class Meta:
        model = Poll
        fields = ['pk', 'name', 'description', 'start_date', 'end_date']


class PollUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['pk', 'name', 'description', 'end_date']


class QuestionPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['pk', 'text', 'poll']


class QuestionPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'text']
