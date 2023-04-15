from django.urls import path
from . import views
# from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('register', views.UserRegister.as_view(), name = 'register'),
    # path('api-token-auth/', auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),

]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls