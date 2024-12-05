# restaurant/urls.py
from django.urls import path
from . import views

""" urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),  
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()), 
]  """


urlpatterns = [
    path('menu/items', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
] 
