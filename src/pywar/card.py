from dataclasses import dataclass
from enum import Enum, auto


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


@dataclass(frozen=True)
class Card:
    rank: Rank
    suit: Suit

    @property
    def value(self):
        return self.rank.value
