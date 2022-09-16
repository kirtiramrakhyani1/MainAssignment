from django.urls import path



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views  import RegAPIView, LogAPIView


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/logout/', LogAPIView.as_view(), name='logout_view'),
    path('api/register/', RegAPIView.as_view())

]