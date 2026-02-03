from django.urls import path
from  .views import admin_dashboard,dress_create,category_create,category_list,category_update,category_delete
urlpatterns = [
  path('dashboard/',admin_dashboard,name='dashboard'),
  path('dress_create',dress_create,name='dress_create'),
  path('category_list',category_list,name='category_list'),
  path('category_create',category_create,name='category_create'),
  path('category_update/<int:pk>/',category_update,name="category_update"),
  path('category_delete/<int:pk>/',category_delete,name='category_delete'),
]
