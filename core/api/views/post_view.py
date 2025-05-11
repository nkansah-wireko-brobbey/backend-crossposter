from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def simple_test(request):
    title = request.data.get('title') 
    content = request.data.get('content')

    return Response({"message":"This is a test it's working!"}, status=status.HTTP_201_CREATED)