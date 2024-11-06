from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def upload_document(request, claim_id):
    return Response({"message": f"Document uploaded for claim {claim_id}"})

@api_view(['GET'])
def view_documents(request, claim_id):
    return Response({"message": f"Documents for claim {claim_id}"})
