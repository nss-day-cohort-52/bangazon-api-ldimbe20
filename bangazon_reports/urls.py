from django.urls import path
from .views import ExpensiveProductList
from .views import FavoriteStores
from .views import PaidOrders

urlpatterns = [
    path('reports/products', ExpensiveProductList.as_view()),
    path('reports/store', FavoriteStores.as_view()),
    path('reports/orders', PaidOrders.as_view()),
]



