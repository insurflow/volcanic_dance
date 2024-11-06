# -----------------------------------------------------------------------------
# Copyright (c) 2024, Insurflow, All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
# -----------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_policies, name='list_policies'),
    path('<int:id>/', views.policy_detail, name='policy_detail'),
]