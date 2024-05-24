from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('token/authentication/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]