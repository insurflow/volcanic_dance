from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_policies(request):
    return Response({"message": "List of policies"})

@api_view(['GET'])
def policy_detail(request, policy_id):
    return Response({"message": f"Details of policy {policy_id}"})

