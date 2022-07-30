from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import MenuViewSet, CurrentDayMenuListView, EmployeeCreateView, RestaurantCreateView, VotingCreateView, \
    VotingDayResultListView

menu_router = routers.DefaultRouter()
menu_router.register(r'(?P<restaurant_id>\d+)', MenuViewSet, basename='menu')

urlpatterns = [
    # JWT
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('v1/today_menu/<int:restaurant_id>/', CurrentDayMenuListView.as_view()),
    path('v1/create_employee/', EmployeeCreateView.as_view()),
    path('v1/create_restaurant/', RestaurantCreateView.as_view()),
    path('v1/voting/', VotingCreateView.as_view()),
    path('v1/voting_results/', VotingDayResultListView.as_view()),
    path('v1/menu/', include(menu_router.urls))
]
