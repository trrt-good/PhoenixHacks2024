from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'hello':'world', 'age':28}
    return Response(person)