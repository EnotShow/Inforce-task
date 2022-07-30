from datetime import datetime

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView

from api.models import Restaurant, MenuPositions, Employee, Votes
from api.serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VotesSerializer


class RestaurantCreateView(CreateAPIView):
    """ View for restaurant creation  """
    model = Restaurant
    serializer_class = RestaurantSerializer
    # permission_classes = [IsAdminUser]


class MenuViewSet(viewsets.ModelViewSet):
    """ ViewSet for view and edit menu """
    model = MenuPositions
    serializer_class = MenuSerializer
    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        return MenuPositions.objects.filter(restaurant_id=self.kwargs.get('restaurant_id'))


class EmployeeCreateView(CreateAPIView):
    """ Employee creation view """
    model = Employee
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAdminUser]


class CurrentDayMenuListView(ListAPIView):
    """ View to get today menu """
    serializer_class = MenuSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = MenuPositions.objects.filter(
            day=datetime.today().isoweekday(),
            restaurant_id=self.kwargs.get('restaurant_id')
        )
        return queryset


class VotingCreateView(CreateAPIView):
    """ View for employee voting """
    model = Votes
    serializer_class = VotesSerializer
    # permission_classes = [IsAuthenticated]


class VotingDayResultListView(ListAPIView):
    """ View to watch voting results """
    models = Votes
    serializer_class = VotesSerializer
    queryset = Votes.objects.filter(date=datetime.today().date())
    # permission_classes = [IsAdminUser]
