from django.urls import path, include
from .views import RegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path("register/",  view=RegistrationView.as_view(), name="register"),
	path("token/", view=TokenObtainPairView.as_view(), name="token_obtain_pair"),
	path("token/refresh", view=TokenRefreshView.as_view(), name="token_refresh"),
	path("auth/", include("rest_framework.urls")),
]
