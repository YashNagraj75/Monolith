import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, cart_id: int, username: str, contents: list[Product], cost: float):
        self.id = cart_id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(self, data):
        return Cart(data['cart_id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    items = []
    for cart_detail in cart_details:
        contents = json.loads(cart_detail['contents'])
        items.extend(contents)

    return [products.get_product(i) for i in items]



def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
