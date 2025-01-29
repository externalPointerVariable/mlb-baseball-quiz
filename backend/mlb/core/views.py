from rest_framework import response, request
from rest_framework.decorators import api_view

@api_view(['GET'])
def welcome(request):
    return response.Response({'message': 'Welcome to MLB API!'})