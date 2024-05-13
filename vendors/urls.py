# vendor_management/urls.py
from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDestroy, PurchaseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy

urlpatterns = [
    path('vendors/', VendorListCreate.as_view(), name='vendor-list-create'),  # Remove 'api/' prefix here
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),  # Remove 'api/' prefix here
    path('purchase_orders/', PurchaseOrderListCreate.as_view(), name='purchase-order-list-create'),  # Remove 'api/' prefix here
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase-order-retrieve-update-destroy'),  # Remove 'api/' prefix here
]
