from datetime import datetime

from rest_framework import serializers

from api.models import MenuPositions, Employee, Restaurant, Votes


class MenuSerializer(serializers.ModelSerializer):
    """ Menu serializer """

    class Meta:
        model = MenuPositions
        fields = ['day', 'dish', 'restaurant_id']


class EmployeeSerializer(serializers.ModelSerializer):
    """ EmployeeSerializer """

    class Meta:
        model = Employee
        fields = ['user']


class RestaurantSerializer(serializers.ModelSerializer):
    """ Restaurant serializer """

    class Meta:
        model = Restaurant
        fields = ['title']


class VotesSerializer(serializers.ModelSerializer):
    """ Votes serializer """
    # I try to do voter field hidden, but I can't

    # voter = serializers.SerializerMethodField()
    # voter = serializers.HiddenField(default=Employee.objects.get(user_id=))
    date = serializers.HiddenField(default=datetime.today().date())

    # def get_voter(self, obj):
    #     print(self.context.get(request).user.id)
    #     return Employee.objects.filter(user_id=self.context.get(request).user.id)

    class Meta:
        model = Votes
        fields = ['voter', 'dish', 'date']
