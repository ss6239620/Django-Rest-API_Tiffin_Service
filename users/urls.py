from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('profile/detail/',UserProfileDetailView.as_view()),
    path('profile/update/',UserProfileUpdateView.as_view()),
    path('register/',UserRegisterView.as_view()),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sellers/',SellerListView.as_view()),
    path('user-lists/',UserListView.as_view()),
    path('user-delete/',UserDeleteView.as_view()),
]
