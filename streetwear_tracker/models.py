"""Data types shared across the package."""

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class Store:
    """A Shopify storefront we poll.

    `currency` is discovered from the store's /cart.js rather than
    hardcoded -- Dover Street Market prices in GBP while the US stores
    price in USD, and products.json never says which.
    """

    domain: str
    name: str
    currency: str


@dataclass(frozen=True)
class Variant:
    """One purchasable size of a product, as seen in a single poll.

    `compare_at_price` is the pre-markdown price when an item is on
    sale, and None otherwise. It is the store telling us directly that
    a discount exists, so we never have to infer one from two numbers
    sitting next to each other.
    """

    variant_id: int
    size: str
    price: float
    compare_at_price: Optional[float]
    available: bool
    sku: Optional[str]

    @property
    def on_sale(self) -> bool:
        return self.compare_at_price is not None and self.compare_at_price > self.price


@dataclass(frozen=True)
class Product:
    """A product and all its variants, as seen in a single poll."""

    store_domain: str
    product_id: int
    handle: str
    title: str
    vendor: Optional[str]
    product_type: Optional[str]
    updated_at: str
    variants: Tuple[Variant, ...]

    @property
    def url(self) -> str:
        return f"https://{self.store_domain}/products/{self.handle}"

    @property
    def in_stock(self) -> bool:
        return any(v.available for v in self.variants)

    @property
    def price_range(self) -> Optional[Tuple[float, float]]:
        """Lowest and highest variant price, or None if there are no variants."""
        prices = [v.price for v in self.variants]
        if not prices:
            return None
        return min(prices), max(prices)
