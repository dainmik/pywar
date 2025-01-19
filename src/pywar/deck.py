from collections.abc import Sequence

from pywar.card import Card


class Deck:
    def __init__(self, cards: list[Card]) -> None:
        self._cards = cards

    @property
    def cards(self):
        return self._cards.copy()

    def split(self):
        middle_index = len(self._cards) // 2
        decks = Deck(self._cards[:middle_index]), Deck(self._cards[middle_index:])
        self._cards = []
        return decks

    def add_to_bottom(self, cards: Sequence[Card]):
        self._cards = [*self._cards, *cards]

    def get_card_from_top(self):
        return self._cards[0]

    def get_cards_from_top(self, number: int):
        return self._cards[0:number]

    def size(self) -> int:
        return len(self._cards)
