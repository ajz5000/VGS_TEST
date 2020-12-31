from django.urls import path
from .views import TransactionListView, TransactionDetailView, add, reveal


urlpatterns = [
    path('', TransactionListView.as_view(), name='index'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='detail'),
    path('add', add, name='add'),
    path('reveal', reveal, name='reveal'),

]