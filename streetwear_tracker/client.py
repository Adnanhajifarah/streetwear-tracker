import requests

def get_currency(domain: str) -> str:
    """Return the currency code a store prices in."""
    cart = requests.get(f"https://'{domain}'/cart.js",timeout=15).json()
    return cart['currency']
