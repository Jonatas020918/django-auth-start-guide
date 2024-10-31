from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import GoogleLoginView, CustomTokenObtainPairView, CustomTokenRefreshView, LogoutView, UserRegistrationView

app_name = 'autenticacao'

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/google/', GoogleLoginView.as_view(), name='google_login'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('oauth/', include('social_django.urls', namespace='social'))
]
