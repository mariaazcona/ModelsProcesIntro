from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.list_products, name='list_products'),
    path('history/', views.purchase_history, name="purchase_history"),
    path('products/<int:item_id>/', views.buy_item, name="buy_item"),
    path('history/delete_purchase/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
    path('products/<int:product_id>/review/', views.add_review, name="add_review"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
