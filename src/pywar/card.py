from enum import Enum, auto
from typing import Final


class Suit(Enum):
    """Card suits sorted from lowest to highest"""

    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


class Rank(Enum):
    """Card ranks sorted from lowest to highest"""

    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()


class Card:
    def __init__(self, rank: Rank, suit: Suit) -> None:
        self.rank: Final = rank
        self.suit: Final = suit

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank.value < other.rank.value

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank.value <= other.rank.value

    def __repr__(self) -> str:
        return f"{type(self).__name__}(rank={self.rank}, suit={self.suit})"
