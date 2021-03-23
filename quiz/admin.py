from django.contrib import admin

# Register your models here.
from django.contrib.admin import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from quiz.models import Question, Answer, Poll, Choice, User


class UserAdmin(BaseUserAdmin):
    list_display = ('username',)


admin.site.register(User, UserAdmin)
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Answer)


