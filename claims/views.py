from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def submit_claim(request):
    return Response({"message": "Claim submitted successfully!"})

@api_view(['GET'])
def list_claims(request):
    return Response({"message": "List of claims"})

@api_view(['GET'])
def claim_detail(request, claim_id):
    return Response({"message": f"Details for claim {claim_id}"})

@api_view(['PUT'])
def update_claim(request, claim_id):
    return Response({"message": f"Claim {claim_id} updated"})
