from rest_framework.views import APIView

from django.http import JsonResponse

from api.models import (
    Category,
    Item
)
from api.serializers import (
    CategorySerializer,
    ItemSerializer
)


# Create your views here.
class CategoryView(APIView):

    """
    List all categories, or create a new category.
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serialzer = CategorySerializer(categories, many=True)
        return JsonResponse(serialzer.data, safe=False)

    def post(self, request, format=None):
        categories = request.data
        serialzer = CategorySerializer(data=categories, many=True)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, safe=False)


class ItemView(APIView):

    """
    List all items, or create a new item.
    """
    def get(self, request, format=None):
        items = Item.objects.all()
        serialzer = ItemSerializer(items, many=True)
        return JsonResponse(serialzer.data, safe=False)

    def post(self, request, format=None):
        items = request.data
        serialzer = ItemSerializer(data=items, many=True)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, safe=False)
