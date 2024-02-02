from django import template

register = template.Library()


@register.filter
def media_path(value):
    """Фильтр для создания маршрута к медиа"""
    return '/media/' + str(value)


@register.simple_tag
def media_path(value):
    """Тег для создания маршрута к медиа"""
    return '/media/' + str(value)
