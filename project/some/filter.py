from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Comment


class PostFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'post': ['in'],
            'user': ['exact'],
            'text': ['icontains'],
            'time_in': ['year', 'month', 'day']
        }
