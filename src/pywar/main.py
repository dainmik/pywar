from pywar.card import Card, Rank, Suit
from pywar.deck import Deck
from pywar.game import Game, GameConfig, Player


def main():
    cards = [Card(rank, suit) for rank in Rank for suit in Suit]
    deck = Deck(cards)

    deck.shuffle()

    player_one_deck, player_two_deck = deck.split()

    game = Game(
        GameConfig(
            player_one=Player(
                name="Player 1",
                deck=player_one_deck,
            ),
            player_two=Player(
                name="Player 2",
                deck=player_two_deck,
            ),
        )
    )

    game_state = game.start()

    print("\n".join(game_state.logs))
