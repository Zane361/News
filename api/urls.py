from . import views
from django.urls import path

urlpatterns = [
    # ----- CATEGORY -----
    path('list-category/', views.list_category, name='list_category'),
    path('detail-category/<int:id>/', views.detail_category, name='detail_category'),
    # ----- REGION -----
    path('list-region/', views.list_region, name='list_region'),
    path('detail-region/<int:id>/', views.detail_region, name='detail_region'),
    # ----- NEW -----
    path('list-new/', views.list_new, name='list_new'),
    path('detail-new/<int:id>/', views.detail_new, name='detail_new'),
]