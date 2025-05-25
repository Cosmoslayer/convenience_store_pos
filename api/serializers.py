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
    class Meta:
        model = Item
        fields = ['id', 'description', 'buying_price',
                  'selling_price', 'stock', 'image',
                  'category_id', 'created_at']

