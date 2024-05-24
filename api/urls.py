from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    # Account paths
    path('account/', views.AccountListCreateAPIView.as_view(),
            name='account-list'),
    path('account/<int:pk>/', views.AccountDetailAPIView.as_view(),
            name='account-detail'),

    # Category paths
    path('category/', views.CategoryListCreateAPIView.as_view(),
            name='category-list'),
    path('category/<int:pk>/', views.CategoryDetailAPIView.as_view(),
            name='category-detail'),
    
    # Transaction paths
    path('transaction/', views.TransactionListCreateAPIView.as_view(),
            name='transaction-list'),
    path('transaction/<int:pk>/', views.TransactionDetailAPIView.as_view(),
            name='transaction-detail'),
]