from django.urls import path
from . import views

urlpatterns = [
    # path("resgistrations/", views.RegistrationsView.as_view(), name="resgistrations"),
    # path("login/", views.LoginView.as_view(), name="login"),
    # path("verify/", views.VerifyEmailView.as_view(), name="verify-email"),
    # path("crul/", views.SpyfuyAPIView.as_view(), name="crul"),
    # path('read_url/', views.URLReaderAPIView.as_view(), name='read-url'),
    path('google/', views.GoogleAuthAPIView.as_view(), name='google-auth')
]