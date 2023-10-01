from django.urls import path

from . import views 

app_name = 'watches'

urlpatterns = [
    path('', views.filtered_items, name='items'), 
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/submit_offer/', views.submit_offer, name='submit_offer'),
    path('watches/category/<str:category_name>/', views.filtered_items, name='watches_by_category'),  
    path('watches/filter/price/', views.filtered_items, name='filtered_watches_by_price'), 
    path('filtered_watches_by_year/', views.filtered_items, name='filtered_watches_by_year'),
    path('search/', views.search_items, name='search_items'),
] 