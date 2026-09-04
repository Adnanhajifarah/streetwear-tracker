"""Data types shared across the package."""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Listing:
    """Details extracted from a single Depop listing page.

    `price` and `currency` are None when the page shows something we
    couldn't read as a single amount. `raw_price` always keeps the
    original string so nothing is lost when parsing gives up.
    """

    url: str
    title: str
    price: Optional[float]
    currency: Optional[str]
    raw_price: str
    brand: Optional[str] = None
    available: Optional[bool] = None

    @property
    def has_price(self) -> bool:
        return self.price is not None

    def __str__(self) -> str:
        if not self.has_price:
            return f"{self.title}\n  price unreadable: {self.raw_price!r}"
        return f"{self.title}\n  {self.currency} {self.price:,.2f}"
