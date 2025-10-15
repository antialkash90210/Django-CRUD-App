from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('item/create/', views.create_item_view, name='create_item'),
    path('item/<int:item_id>/update/', views.update_item_view, name='update_item'),
    path('item/<int:item_id>/delete/', views.delete_item_view, name='delete_item'),
    path('', views.home_view, name='home'),  # Add home view

]
