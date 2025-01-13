# PyWar

## ❓ What is PyWar?

PyWar is a CLI ["War" card game](https://en.wikipedia.org/wiki/War_(card_game)) simulator.

The goal is to design the game in a way that is as flexible as possible so that it would be easy to eventually add all the extra features under the "Future ideas" section.

## 🏆 Features

- [ ] Fully functional game logic for "War" according to the [rules](https://en.wikipedia.org/wiki/War_(card_game)#Rules).
- [ ] Once started, the game runs until the end and prints out the result to stdout.
- [ ] The output includes clear round-by-round results and the final winner.

## 💡 Feature Ideas

- [ ] Optional variations of the rules (e.g., multiple cards in a "war").
- [ ] Allow interactive user input so that a person can play against the computer or two players can take turns
- [ ] Support multiple players
- [ ] Accept any number of cards

## 🎮 Requirements

- Card rank (from best to worst):
    - [ ] A K Q J 10 9 8 7 6 5 4 3 2
    - [ ] Joker (optional)

- [ ] Game uses a standard deck of 52 playing cards.
- [ ] At the start of the game, initialize the deck in a random order.
- [ ] Divide the deck evenly among players. These decks are called ACTIVE decks.

- Battle phase:
    - [ ] All players reveal the top card of their deck.
    - [ ] The player with the highest card wins and moves the won cards to their INACTIVE deck.
        - [ ] Aces are the highest (if Joker is not in play) and suits are ignored.
    - [ ] If the two cards played are of equal value, then there is a War.

- War phase
    - [ ] All players place the next card from their ACTIVE deck face down.
    - [ ] And also place one more card from their ACTIVE deck face up.
    - [ ] The owner of the higher face-up card wins the war and adds all the cards on the table to their INACTIVE deck.
    - [ ] If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

- [ ] If a player runs out of ACTIVE cards, shuffle the INACTIVE deck, and this deck becomes ACTIVE.
- [ ] If a player runs out of ACTIVE cards, and there are no cards in their INACTIVE deck, they lose.

## 💪 Contributing

Please refer to [CONTRIBUTING](./CONTRIBUTING.md) for detailed instructions.

## 🔑 License

[MIT](./LICENSE)