
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('pages/', views.get_pages, name='pages'),
    path('pages/new/', views.create_page, name='create_page'),
    path('pages/<int:page_id>/delete/', views.delete_page, name='delete_page'),
    path('messages/', views.messages_view, name='messages'),
    
]
