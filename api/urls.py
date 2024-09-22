from django.urls import path, include
import views as v
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path("register/",  view=v.RegistrationView.as_view(), name="register"),
	path("token/", view=TokenObtainPairView.as_view(), name="token_obtain_pair"),
	path("token/refresh", view=TokenRefreshView.as_view(), name="token_refresh"),
	path("auth/", include("rest_framework.urls")),
	path("categories/",  view=v.CategoryListCreate.as_view(), name="categories"),
	path("categories/<int:pk>", view=v.CategoryDelete.as_view(), name="category_delete"),
	path("todos/",  view=v.TodoListCreate.as_view(), name="todos"),
	path("todos/<int:id>", view=v.TodoDelete.as_view(), name="todo_delete"),
	
]
