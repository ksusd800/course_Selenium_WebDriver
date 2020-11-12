import pytest
import time


def test_can_add_delete(app):
    old_count = app.count_items_in_cart()
    app.add_product_in_cart()
    app.delete_product_from_cart()
    new_count = app.count_items_in_cart()
    assert old_count == new_count
