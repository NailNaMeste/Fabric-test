from rest_framework import status, exceptions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from quiz.models import Poll, Question, Choice, Answer
from quiz.serializers import PollUpdateSerializer, QuestionSerializer, PollCreateSerializer, ChoiceSerializer, \
    QuestionPostSerializer, QuestionPutSerializer, AnswerSerializer, ChoicePostSerializer


class GetCreateAllPoll(APIView):

    def get(self, request):
        poll = Poll.objects.all()
        last_point = PollUpdateSerializer(poll, many=True)
        return Response(last_point.data)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = PollCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollDetail(APIView):

    def get(self, request, pid):
        poll = Poll.objects.filter(pk=pid)
        last_point = PollUpdateSerializer(poll, many=True)
        return Response(last_point.data)

    @permission_classes([IsAuthenticated])
    def put(self, request, pid):
        poll = Poll.objects.get(pk=pid)
        serializer = PollUpdateSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pid):
        poll = Poll.objects.filter(pk=pid)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionCreateAPIView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, pid):
        request.data.update({"poll": pid})
        serializer = QuestionPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(APIView):

    def get(self, request, pid, qid):
        poll = Question.objects.filter(poll=pid).filter(pk=qid)
        serializer = QuestionSerializer(poll, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        qid = kwargs.get('qid')

        request.data.update({"question": qid})

        get_choice = Choice.objects.filter(question=qid)
        for get_ch in get_choice:
            if int(get_ch.pk) == int(request.data.get('choice_pk')):
                request.data.update({'choice_pk': get_ch.pk, 'choice_text': get_ch.text})

        serializer = AnswerSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def put(self, request, pid, qid):
        question = Question.objects.get(pk=qid)
        serializer = QuestionPutSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pid, qid):
        question = Question.objects.get(pk=qid)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckAnswerAPIView(APIView):

    def get(self, request, anon_id):
        queryset = Answer.objects.filter(anon_id=anon_id)
        serializer = AnswerSerializer(queryset, many=True)

        get_question = queryset.values('question')

        for question_id in get_question:
            question_text = Question.objects.filter(pk=question_id['question']).values('text', 'pk')
            get_poll = Poll.objects.filter(question=question_id['question']).values('name')

        try:
            context = {
                'poll_name': [poll_name for poll_name in get_poll],
                'question_text': question_text,
                'choice': serializer.data
            }
        except UnboundLocalError:
            raise NotFound
        return Response(context)


class ChoicePost(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request, **kwarg):
        request.data.update({"question": kwarg.get('qid')})
        serializer = ChoicePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
