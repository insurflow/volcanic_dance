# -----------------------------------------------------------------------------
# Copyright (c) 2024, Insurflow, All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
# -----------------------------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [
    path('<int:claim_id>/upload/', views.upload_document, name='upload_document'),
    path('<int:claim_id>/documents/', views.view_documents, name='view_documents'),
]