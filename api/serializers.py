from rest_framework import serializers

from api.models import (
    Category,
    Item
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'created_at']


class ItemSerializer(serializers.ModelSerializer):
    buyingPrice = serializers.DecimalField(max_digits=11, decimal_places=2,
                                           source='buying_price')
    sellingPrice = serializers.DecimalField(max_digits=11, decimal_places=2,
                                            source='selling_price')
    categoryId = serializers.IntegerField(source='category_id', required=False)
    createdAt = serializers.DateTimeField(source='created_at', required=False)

    class Meta:
        model = Item
        fields = ['id', 'description', 'buyingPrice', 'sellingPrice', 'stock',
                  'image', 'categoryId', 'createdAt']
