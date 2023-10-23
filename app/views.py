# end points
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, renderers
from .models import Boat, Slip
from .serializers import BoatSerializer, SlipSerializer
import boto3



@api_view(['GET', 'POST'])
def boat_list(request):
    renderer_classes = [renderers.JSONRenderer]
    db = boto3.resource('dynamodb')
    table = db.Table('boats')
    # get all boat python objects
    # serialize them to json
    # return json data
    if request.method == "GET":
        boats = table.scan()
        return Response({'boats': boats.get('Items')})
    elif request.method == 'POST':
        try:
            table.put_item(Item=request.data)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Failed to insert'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


def slip_list(request):
    slips = Slip.objects.all()
    serializer = SlipSerializer(slips, many=True)
    return JsonResponse(serializer.data, safe=False)