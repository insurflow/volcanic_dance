# -----------------------------------------------------------------------------
# Copyright (c) 2024, Insurflow, All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
# -----------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path('reset-password/', views.reset_password, name='reset_password'),
    path('user/', views.user_profile, name='user_profile'),
]