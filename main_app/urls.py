from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wines/', views.wines_index, name='index'),
    path('wines/<int:wine_id>/', views.wines_detail, name='detail'),
    path('wines/create/', views.WineCreate.as_view(), name='wines_create'),
    path('wines/<int:pk>/update/', views.WineUpdate.as_view(), name='wines_update'),
    path('wines/<int:pk>/delete/', views.WineDelete.as_view(), name='wines_delete'),
    path('wines/<int:wine_id>/add_year/', views.add_year, name='add_year'),
    path('wines/<int:wine_id>/assoc_food/<int:food_id>', views.assoc_food, name='assoc_food'),
    path('wines/<int:wine_id>/remove_food/<int:food_id>', views.remove_food, name='remove_food'),
    path('wines/<int:wine_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
] 
