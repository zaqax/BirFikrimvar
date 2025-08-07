from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/like/', views.post_like, name='post_like'),
    path('<int:pk>/unlike/', views.post_unlike, name='post_unlike'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]