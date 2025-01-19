import random
from collections.abc import Sequence

from pywar.card import Card


class Deck:
    def __init__(self, cards: list[Card]) -> None:
        self._cards = cards

    @property
    def cards(self):
        return tuple(self._cards)

    def split(self):
        middle_index = len(self._cards) // 2
        decks = Deck(self._cards[:middle_index]), Deck(self._cards[middle_index:])
        self._cards = []
        return decks

    def shuffle(self):
        self._cards = random.sample(self._cards, len(self._cards))

    def add_to_bottom(self, cards: Sequence[Card]):
        self._cards = [*self._cards, *cards]

    def get_card_from_top(self):
        card = self._cards[0]
        self._cards = self._cards[1:]
        return card

    def get_cards_from_top(self, number: int):
        cards = self._cards[0:number]
        self._cards = self._cards[number:]
        return cards

    def size(self) -> int:
        return len(self._cards)
