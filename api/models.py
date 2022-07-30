from django.contrib.auth.models import User
from django.db import models


class Restaurant(models.Model):
    """ Restaurant model """
    title = models.CharField(max_length=50, verbose_name="Назва")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторан'


class Dishes(models.Model):
    """ Dishes what users can be votes and what been added to the menu """
    title = models.CharField(max_length=25, verbose_name="Назва")
    about = models.TextField(verbose_name='Склад')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Страви'
        verbose_name_plural = 'Страви'


class MenuPositions(models.Model):
    """ Menu positions model """
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.IntegerField(verbose_name='День')
    dish = models.ForeignKey(
        Dishes,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )

    def __str__(self):
        return f"{self.dish.title}, {self.day}"

    class Meta:
        verbose_name = 'Позиції меню'
        verbose_name_plural = 'Позиції меню'


class Employee(models.Model):
    """ Employee model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Співробітники'
        verbose_name_plural = 'Співробітники'


class Votes(models.Model):
    """ Employee votes model """
    voter = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.voter

    class Meta:
        verbose_name = 'Голосування'
        verbose_name_plural = 'Голосування'
