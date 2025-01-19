from pywar.card import Card, Rank, Suit
from pywar.deck import Deck
from pywar.game import Game, GameConfig, GameResult, GameState, Player


def test_game_returns_initial_state():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]
    deck = Deck(cards)

    player_one_deck, player_two_deck = deck.split()

    player_one = Player(
        name="Player 1",
        deck=player_one_deck,
    )
    player_two = Player(
        name="Player 2",
        deck=player_two_deck,
    )

    game = Game(
        GameConfig(
            player_one=player_one,
            player_two=player_two,
        )
    )

    game_state = game.start()

    assert game_state == GameState(
        round_count=1,
        player_one=player_one,
        player_two=player_two,
        logs=[],
        result=GameResult(state="RUNNING"),
    )


def test_get_winner_when_players_have_cards_remaining_should_return_none():
    player_one = Player(
        name="Player 1",
        deck=Deck([Card(Rank.QUEEN, Suit.HEARTS)]),
    )
    player_two = Player(
        name="Player 2",
        deck=Deck([Card(Rank.JACK, Suit.SPADES)]),
    )

    assert Game._get_winner(player_one, player_two) is None


def test_get_winner_when_both_players_do_not_have_cards_remaining_should_return_none():
    player_one = Player(
        name="Player 1",
        deck=Deck([]),
    )
    player_two = Player(
        name="Player 2",
        deck=Deck([]),
    )

    assert Game._get_winner(player_one, player_two) is None


def test_get_winner_when_one_player_does_not_have_cards_remaining_should_return_other_player_as_winner():
    player_one = Player(
        name="Player 1",
        deck=Deck([Card(Rank.QUEEN, Suit.HEARTS)]),
    )
    player_two = Player(
        name="Player 2",
        deck=Deck([]),
    )

    assert Game._get_winner(player_one, player_two) is player_one
