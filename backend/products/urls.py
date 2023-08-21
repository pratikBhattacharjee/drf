from django.urls import path

from .views import ProductDetailAPIView, ProductCreateAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='detail'),
    path('', ProductCreateAPIView.as_view(), name='create'),
]