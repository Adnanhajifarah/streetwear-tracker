"""The storefronts this tracker polls.

Currency is deliberately absent here -- it comes from each store's
/cart.js at poll time. Hardcoding it is how you end up reporting a
GBP price as dollars.
"""

STORES = (
    ("undefeated.com", "Undefeated"),
    ("shop.doverstreetmarket.com", "Dover Street Market"),
    ("bdgastore.com", "Bodega"),
)
