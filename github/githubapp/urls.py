from django.urls import path,include
from .import views
from rest_framework_simplejwt.views import(
TokenObtainPairView,
TokenRefreshView
)
from.views import Home
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("accounts/", include("allauth.urls")),
    path("", Home.as_view(), name="home"),
    path('github_trending_repository/',views.github_trending_repos, name='github_trending_repos'),
]
