from django.urls import path
from .views import get_transaction

urlpatterns = [
    path('transactions/<int:id>/', get_transaction) # TODO add the function
]
