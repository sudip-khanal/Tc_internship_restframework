from django.shortcuts import get_object_or_404
from apps.api.models import Product
from apps.api.serializers import ProductSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_summary="List all the product",
    operation_description="This endpont return all the list of product"
)
@api_view(['GET'])
def get_products(self):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    operation_summary="Create New Product",
    operation_description="This endpont create a new product",
    request_body=ProductSerializers
)
@api_view(['POST'])
def create_product(request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get', 
    operation_summary="Get Product By Id",
    operation_description="This endpont return a product by id"
)
@api_view(['GET'])
def get_product(self, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)


@swagger_auto_schema(
    method='put',
    operation_summary="Update Product",
    operation_description="This endpont update a product by id",
    request_body=ProductSerializers
)
@api_view(['PUT'])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializers(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='delete',
    operation_summary="Delete Product",
    operation_description="This endpont delete product by id",
)
@api_view(['DELETE'])
def delete_product(self, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response(status=status.HTTP_200_OK)

