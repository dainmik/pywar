import pytest

from pywar.card import Card, Rank, Suit


def test_there_should_be_four_card_suits():
    assert len(Suit) == 4


def test_there_should_be_thirteen_card_ranks():
    assert len(Rank) == 13


@pytest.mark.parametrize(
    "rank",
    [
        *Rank,
    ],
)
@pytest.mark.parametrize(
    "suit",
    [
        *Suit,
    ],
)
def test_card_can_be_instantiated_with_correct_rank_and_suite(rank: Rank, suit: Suit):
    card = Card(rank, suit)

    assert card.rank == rank
    assert card.suit == suit


@pytest.mark.parametrize(
    "first_card, second_card, expected",
    [
        (
            Card(Rank.TWO, Suit.CLUBS),
            Card(Rank.ACE, Suit.CLUBS),
            True,
        ),
        (
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.TWO, Suit.CLUBS),
            False,
        ),
    ],
)
def test_card_less_than_operator_returns_correct_result(
    first_card: Card,
    second_card: Card,
    expected: bool,
):
    assert (first_card < second_card) == expected
