from django.urls import path
from . import views

url_patterns = [
    # ----- AUTH -----
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('register/', views.register, name='register'),
    # ----- CATEGORY -----
    path('category-create/', views.category_create, name='category_create'),
    path('category-list/', views.category_list, name='category_list'),
    path('category-update/<int:id>', views.category_update, name='category_update'),
    path('category-delete/<int:id>', views.category_delete, name='category_delete'),
]