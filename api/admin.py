from django.contrib import admin

from api.models import Restaurant, Dishes, MenuPositions, Employee, Votes


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'about',)


@admin.register(MenuPositions)
class MenuPositionsAdmin(admin.ModelAdmin):
    list_display = ('dish', 'day',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Votes)
class VotesAdmin(admin.ModelAdmin):
    list_display = ('voter', 'dish')
