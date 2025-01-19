from dataclasses import dataclass
from typing import Literal

from pywar.deck import Deck


@dataclass(frozen=True, kw_only=True)
class Player:
    name: str
    deck: Deck


@dataclass(frozen=True, kw_only=True)
class GameResult:
    state: Literal["RUNNING", "FINISHED"]
    winner: Player | None = None


@dataclass(frozen=True, kw_only=True)
class GameState:
    round_count: int = 1
    player_one: Player
    player_two: Player
    logs: list[str]
    result: GameResult


@dataclass(frozen=True, kw_only=True)
class GameConfig:
    player_one: Player
    player_two: Player
    max_rounds: int = 30


class Game:
    def __init__(self, config: GameConfig) -> None:
        self._config = config

    def start(self):
        state = GameState(
            player_one=self._config.player_one,
            player_two=self._config.player_two,
            logs=[],
            result=GameResult(state="RUNNING"),
        )

        while state.result.state != "FINISHED":
            state = self._update(
                state=state,
                max_rounds=self._config.max_rounds,
            )

        return state

    @classmethod
    def _update(cls, *, state: GameState, max_rounds: int):
        logs = [*state.logs]

        player_one = state.player_one
        player_two = state.player_two

        if winner := cls._get_winner(player_one, player_two):
            return GameState(
                round_count=state.round_count,
                player_one=player_one,
                player_two=player_two,
                logs=[
                    *logs,
                    f"{winner.name} wins the game!",
                ],
                result=GameResult(
                    state="FINISHED",
                    winner=winner,
                ),
            )

        if state.round_count == max_rounds:
            return GameState(
                round_count=state.round_count,
                player_one=player_one,
                player_two=player_two,
                logs=[
                    *logs,
                    f"Round {state.round_count} has been reached. Peace has been negotiated! The war is over!",
                ],
                result=GameResult(state="FINISHED"),
            )

        logs.extend(
            [
                "",
                f"Battle round {state.round_count} begins!",
            ]
        )

        player_one_card = player_one.deck.get_card_from_top()
        player_two_card = player_two.deck.get_card_from_top()

        logs.extend(
            [
                "Players make their moves:",
                f"- {player_one.name}: plays {player_one_card}.",
                f"- {player_two.name}: plays {player_two_card}.",
            ]
        )

        if player_one_card.value > player_two_card.value:
            player_one.deck.add_to_bottom(
                [
                    player_one_card,
                    player_two_card,
                ]
            )
            logs.append(f"{player_one.name} wins the round!")
        elif player_one_card.value < player_two_card.value:
            player_two.deck.add_to_bottom(
                [
                    player_one_card,
                    player_two_card,
                ]
            )
            logs.append(f"{player_two.name} wins the round!")
        else:
            # TODO: Add support for war scenario
            pass

        logs.extend(
            [
                "Cards remaining:",
                f"- {player_one.name}: {player_one.deck.size()} cards.",
                f"- {player_two.name}: {player_two.deck.size()} cards.",
            ]
        )

        return GameState(
            round_count=state.round_count + 1,
            player_one=player_one,
            player_two=player_two,
            logs=logs,
            result=GameResult(state="RUNNING"),
        )

    @classmethod
    def _get_winner(cls, player_one: Player, player_two: Player):
        players = [player_one, player_two]

        players_with_cards = [player for player in players if player.deck.size() > 0]

        if len(players_with_cards) == 1:
            return players_with_cards[0]

        return None
