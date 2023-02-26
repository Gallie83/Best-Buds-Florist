from django import template


register = template.Library()

# Returns subtotal of each items price by quantity


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
