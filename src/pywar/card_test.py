import pytest

from pywar.card import Card, Rank, Suit


def test_there_should_be_four_card_suits():
    assert len(Suit) == 4


def test_there_should_be_thirteen_card_ranks():
    assert len(Rank) == 13


def test_card_can_be_instantiated_with_correct_rank_and_suite():
    card = Card(Rank.ACE, Suit.DIAMONDS)

    assert card.rank == Rank.ACE
    assert card.suit == Suit.DIAMONDS


@pytest.mark.parametrize(
    "first_card, second_card",
    [
        pytest.param(
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.EIGHT, Suit.HEARTS),
            id="Both card values should be equal when their ranks and suits are the same",
        ),
        pytest.param(
            Card(Rank.EIGHT, Suit.DIAMONDS),
            Card(Rank.EIGHT, Suit.HEARTS),
            id="Both card values should be equal when their ranks are the same but suits are different",
        ),
    ],
)
def test_card_value_should_be_equal(first_card: Card, second_card: Card):
    assert first_card.value == second_card.value


@pytest.mark.parametrize(
    "first_card, second_card",
    [
        pytest.param(
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.EIGHT, Suit.HEARTS),
            id="First card value should be greater when its rank is greater and the suits are the same",
        ),
        pytest.param(
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.EIGHT, Suit.HEARTS),
            id="First card value should be greater when its rank is greater and the suits are different",
        ),
    ],
)
def test_first_card_value_should_be_greater_than_second_card_value(
    first_card: Card, second_card: Card
):
    assert first_card.value > second_card.value
