from enum import StrEnum, auto
from typing import Final


class Suit(StrEnum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


class Rank(StrEnum):
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

    def __repr__(self) -> str:
        return f"{type(self).__name__}(rank={self.rank}, suit={self.suit})"
