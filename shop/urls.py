from django.urls import path

from .views import (
    CategoryListView,
    ProductListView,
    SellerProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    InvoiceCreateView,
    InvoiceListView,
    CategoryCreateView,
    CategoryDeleteView,
    SubcategoryCreateView,
    SubcategoryDeleteView,
)

urlpatterns=[
    path('categories/',CategoryListView.as_view()),
    path('products/',ProductListView.as_view()),
    path('products/seller/',SellerProductListView.as_view()),
    path('products/detail/',ProductDetailView.as_view()),
    path('products/create/',ProductCreateView.as_view()),
    path('products/update/',ProductUpdateView.as_view()),
    path('products/delete/',ProductDeleteView.as_view()),
    path('invoices/create/',InvoiceCreateView.as_view()),
    path('invoices/list/',InvoiceListView.as_view()),
    path('categories/create/',CategoryCreateView.as_view()),
    path('categories/delete/',CategoryDeleteView.as_view()),
    path('subcategories/create/',SubcategoryCreateView.as_view()),
    path('subcategories/delete/',SubcategoryDeleteView.as_view()),
]