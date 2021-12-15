# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import (LogoutView, PasswordResetCompleteView,
PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, 
PasswordResetConfirmView,PasswordResetCompleteView)

from .forms import UserPasswordResetForm, UserPasswordChangeForm


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),


    path('password_reset/', PasswordResetView.as_view(
    template_name='forgot-password.html',
    form_class=UserPasswordResetForm),name='reset_password'),

    path("reset_password_sent/", 
    PasswordResetDoneView.as_view(template_name="password_reset_sent.html",), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
    template_name="reset-password.html",
    form_class=UserPasswordChangeForm), name="password_reset_confirm"),

    path("reset_password_complete/", PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),

]





