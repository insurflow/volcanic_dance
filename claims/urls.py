# -----------------------------------------------------------------------------
# Copyright (c) 2024, Insurflow, All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
# -----------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_claim, name='submit_claim'),
    path('<int:id>/', views.claim_detail, name='claim_detail'),
    path('<int:id>/update/', views.update_claim, name='update_claim'),
]