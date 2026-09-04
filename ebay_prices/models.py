"""Data types shared across the package."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Listing:
    """Details extracted from a single eBay listing page.

    `price` and `currency` are None when the page shows something that
    isn't a single fixed amount -- auction ranges, "See details", or a
    layout we couldn't read. `raw_price` always keeps the original
    string so nothing is lost when parsing gives up.
    """

    url: str
    title: str
    price: Optional[float]
    currency: Optional[str]
    raw_price: str

    @property
    def has_price(self) -> bool:
        return self.price is not None

    def __str__(self) -> str:
        if not self.has_price:
            return f"{self.title}\n  price unreadable: {self.raw_price!r}"
        return f"{self.title}\n  {self.currency} {self.price:,.2f}"
