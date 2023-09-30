from django.urls import path

from . import views 

app_name = 'watches'

urlpatterns = [
    path('', views.filtered_items, name='items'),  # Change to 'items'
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/submit_offer/', views.submit_offer, name='submit_offer'),
    path('watches/category/<str:category_name>/', views.filtered_items, name='watches_by_category'),  # Change to 'filtered_items'
    path('watches/filter/price/', views.filtered_items, name='filtered_watches_by_price'),  # Change to 'filtered_items'
    path('filtered_watches_by_year/', views.filtered_items, name='filtered_watches_by_year'),
    path('search/', views.search_items, name='search_items'),
    path('watches/category/<str:category_name>/', views.watches_by_category, name='watches_by_category'),

] 