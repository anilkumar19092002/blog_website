from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/'), name='root-redirect'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post/new/', views.create_post, name='post-create'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/update/', views.update_post, name='post-update'),
    path('post/<int:pk>/delete/', views.delete_post, name='post-delete'),
    path('post/<int:pk>/like/', views.like_post, name='like-post'),
]