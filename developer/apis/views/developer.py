from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.response import Response

from ..serializers.developer import DeveloperSerializer
from developer.models import Developer


class DeveloperViewSet(APIView):
    """
    API View Function To Get, Update and Create Developers
    """
    def get(self, request): #, *args, **kwargs):
        # import pdb; pdb.set_trace()
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        data = serializer.data
        # import pdb; pdb.set_trace()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        state = status.HTTP_406_NOT_ACCEPTABLE
        data = {
            "STATUS": "ERROR"
        }
        serializer = DeveloperSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            state = status.HTTP_201_CREATED
            data = {
                "STATUS": "OK"
            }
        else:
            data["ERROR"] = serializer.errors
            # import pdb; pdb.set_trace()
        return Response(data, status=state)
