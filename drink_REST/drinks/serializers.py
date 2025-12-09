from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Drink
    fields = ['id' , 'name' , 'description']

  def __str__(self):
    return self.name