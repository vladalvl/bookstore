from django import template
from books.models import Category, Genre


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()







