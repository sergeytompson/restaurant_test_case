from django.db.models import Prefetch
from rest_framework import generics

from .models import Food, FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryList(generics.ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.filter(
        id__in=Food.objects.values_list("category")
    ).prefetch_related(Prefetch("food", queryset=Food.objects.all()))
