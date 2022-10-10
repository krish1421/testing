from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
  path("get-details/",UserDetailAPI.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]