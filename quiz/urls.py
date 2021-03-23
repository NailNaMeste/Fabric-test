from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

router = routers.SimpleRouter()




urlpatterns = [
    path('poll/', views.GetCreateAllPoll.as_view(), name='index'),  # get, создать опрос
    path('poll/<int:pid>/', views.PollDetail.as_view()),    # put, delete опрос
    path('poll/<int:pid>/question/', views.QuestionCreateAPIView.as_view()),
    path('poll/<int:pid>/question/<int:qid>/', views.QuestionViewSet.as_view()),  #
    path('poll/<int:pid>/question/<int:qid>/post_choice/', views.ChoicePost.as_view()),
    path('answers/<int:anon_id>/', views.CheckAnswerAPIView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('poll/create', views.CreatePollAPIView.as_view(), name='question')
]
urlpatterns += router.urls
''','''