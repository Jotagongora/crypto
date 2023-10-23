from django.urls import path
from . import views

urlpatterns = [
    path('get_binance_market_data/', views.get_binance_market_data, name='get_binance_market_data'),
]
