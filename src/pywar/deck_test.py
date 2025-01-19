import pytest

from pywar.card import Card, Rank, Suit
from pywar.deck import Deck


@pytest.fixture
def deck_with_52_cards():
    return Deck([Card(rank, suit) for rank in Rank for suit in Suit])


def test_initial_card_deck_contains_52_cards(deck_with_52_cards: Deck):
    assert deck_with_52_cards.size() == 52


def test_deck_returns_tuple_of_cards():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]

    deck = Deck(cards)

    assert deck.cards == tuple(cards)


def test_deck_shuffle_should_return_cards_in_different_order():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]

    deck = Deck(cards)
    deck.shuffle()

    assert deck.cards != tuple(cards)


def test_deck_can_be_split_in_two(deck_with_52_cards: Deck):
    deck_one, deck_two = deck_with_52_cards.split()

    assert deck_one.size() == 26
    assert deck_two.size() == 26
    assert deck_with_52_cards.size() == 0


def test_deck_get_card_from_top_returns_correct_card():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]
    deck = Deck(cards)

    assert deck.get_card_from_top() == cards[0]


def test_deck_get_card_from_top_removes_card_from_deck():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]
    deck = Deck(cards)

    deck.get_card_from_top()

    assert cards[0] not in deck.cards


def test_deck_get_cards_from_top_returns_correct_cards():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]
    deck = Deck(cards)

    assert deck.get_cards_from_top(2) == [cards[0], cards[1]]


def test_deck_get_cards_from_top_removes_card_from_deck():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]
    deck = Deck(cards)

    deck.get_cards_from_top(2)

    assert cards[0] not in deck.cards
    assert cards[1] not in deck.cards


def test_deck_add_one_card_to_bottom_of_deck(deck_with_52_cards: Deck):
    cards_to_add = [
        Card(Rank.JACK, Suit.DIAMONDS),
    ]

    initial_deck_size = deck_with_52_cards.size()
    deck_with_52_cards.add_to_bottom(cards_to_add)

    assert deck_with_52_cards.size() == initial_deck_size + 1
    assert deck_with_52_cards.cards[-1] == cards_to_add[0]


def test_deck_add_two_card_to_bottom_of_deck(deck_with_52_cards: Deck):
    cards_to_add = [
        Card(Rank.JACK, Suit.DIAMONDS),
        Card(Rank.KING, Suit.CLUBS),
    ]

    initial_deck_size = deck_with_52_cards.size()
    deck_with_52_cards.add_to_bottom(cards_to_add)

    assert deck_with_52_cards.size() == initial_deck_size + 2
    assert deck_with_52_cards.cards[-2:] == tuple(cards_to_add)
