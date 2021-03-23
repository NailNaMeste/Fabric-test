from abc import ABC

from django.urls import path
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


class MyTokenObtainPairSerializer(TokenObtainPairSerializer, ABC):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


urlpatterns = [
    path('poll/', views.GetCreateAllPoll.as_view(), name='index'),  # get, создать опросы
    path('poll/<int:pid>/', views.PollDetail.as_view()),    # put, delete, get опрос
    path('poll/<int:pid>/question/', views.QuestionCreateAPIView.as_view()),  # Создать вопрос
    path('poll/<int:pid>/question/<int:qid>/', views.QuestionViewSet.as_view()),  # GET PUT DELETE вопрос,
                                                                                  # POST ответить на вопрос

    path('poll/<int:pid>/question/<int:qid>/post_choice/', views.ChoicePost.as_view()),  # POST Создать ответ
    path('answers/<int:anon_id>/', views.CheckAnswerAPIView.as_view()),  # GET узреть свои ответы

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # GET simplejwt token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

