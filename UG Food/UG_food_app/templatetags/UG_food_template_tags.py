from django import template
from UG_food_app.models import Category

register = template.Library()

@register.inclusion_tag('UG_food/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}