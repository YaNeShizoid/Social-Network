from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignupUserView.as_view(), name='signup'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('friend-request/<int:id>/', views.send_friend_request, name='send-friend-request'),
    path('accept-friend-request/<int:id>/', views.accept_friend_request, name='accept-friend-request'),
    path('users/', views.UsersListView.as_view(), name='users-list'),
    path('activate/<uidb64>/<token>', views.ActivateView.as_view(), name='activate'),
]