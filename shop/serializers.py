from rest_framework import serializers

from .models import Category, Subcategory, Product, Invoice


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['title', 'slug']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['title', 'slug', 'subcategories']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer(source="subcategory.category")
    subcategory = SubcategorySerializer()
    seller = serializers.CharField(source="owner.username")
    seller_latitude = serializers.CharField(source="owner.profile.latitude")
    seller_longitude = serializers.CharField(source="owner.profile.longitude")

    class Meta:
        model = Product
        fields = [
            'seller',
            'seller_latitude',
            'seller_longitude',
            'slug',
            'title',
            'price',
            'description',
            'quantity_type',
            'quantity',
            'thumbnail',
            'category',
            'subcategory'
        ]


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'user', 'total_cost', 'summary', 'billing_address', 'shipping_address', 'date']