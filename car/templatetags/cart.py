from django import template

register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(car, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == car.id:
            return True
    return False


@register.filter (name='cart_quantity')
def cart_quantity(car, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == car.id:
            return cart.get (id)
    return 0


@register.filter (name='price_total')
def price_total(car, cart):
    return car.price * cart_quantity (car, cart)


@register.filter (name='total_cart_price')
def total_cart_price(cars, cart):
    sum = 0
    for c in cars:
        sum += price_total (c, cart)

    return sum
