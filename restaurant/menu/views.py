from django.db.models import Count, Q
from rest_framework import generics

from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryList(generics.ListAPIView):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.annotate(
        cnt_food=Count("food", filter=Q(food__is_publish=True))
    ).filter(
        cnt_food__gt=0
    ).prefetch_related("food__additional")
