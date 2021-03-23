from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from quiz.models import Question, Answer, Poll, Choice, User


class UserAdmin(BaseUserAdmin):
    list_display = ('username',)


admin.site.register(User, UserAdmin)
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Answer)


