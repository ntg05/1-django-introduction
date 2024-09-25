from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import DishSerializer
from store.models import Dish



class DishViewSet(APIView):
    def get(self, request):
        queryset = Dish.objects.all()

        serializer_for_queryset = DishSerializer(
            instance=queryset,
            many=True,
        )

        return Response(serializer_for_queryset.data)

    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
