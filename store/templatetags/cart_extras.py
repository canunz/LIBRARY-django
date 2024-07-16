# store/templatetags/cart_extras.py

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplica el valor por el argumento."""
    try:
        return value * arg
    except (TypeError, ValueError):
        return ''

@register.filter
def sum_total(items):
    """Suma el total de un conjunto de objetos."""
    return sum(item.book.price * item.quantity for item in items)
