# PyWar

## ❓ What is PyWar?

PyWar is a CLI ["War" card game](https://en.wikipedia.org/wiki/War_(card_game)) simulator.

## 🏆 Features

- [ ] Fully functional game logic for "War" according to the [rules](https://en.wikipedia.org/wiki/War_(card_game)#Rules).
- [x] Once started, the game runs until the end and prints out the result to stdout.
- [x] The output includes clear round-by-round results and the final winner.

## 🎮 Requirements

- Card rank (from best to worst):
    - [x] A K Q J 10 9 8 7 6 5 4 3 2

- Game variations:
    - [ ] Automatic War - Laying down a two of any suit causes a War to be declared.
    - [ ] Three cards - Many play with three cards being played face-down during a war.
    - [ ] Peace - The opposite of War, in that the lowest card always wins.
    - [ ] Underdog - The losing player of a War steals the victory if one of their three discard cards is a Jack.

- [x] Game uses a standard deck of 52 playing cards.
- [x] At the start of the game, initialize the deck in a random order.
- [x] Divide the deck evenly among players.

- Battle phase:
    - [x] All players reveal the top card of their deck.
    - [x] The player with the highest card wins and moves the won cards to the bottom of their deck.
        - [x] Aces are the highest and suits are ignored.
    - [ ] If the two cards played are of equal value, then there is a War.

- War phase
    - [ ] All players place the next card from their deck face down.
        - [ ] Option to configure the game to require 3 face-down cards
    - [ ] And also place one more card from their deck face up.
    - [ ] The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck.
    - [ ] If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

- [x] [In Battle phase] If a player runs out of cards (they don't have enough cards to make the next move), they lose.
- [ ] [In war phase] If a player runs out of cards (they don't have enough cards to make the next move), they lose.

## 💪 Contributing

Please refer to [CONTRIBUTING](./CONTRIBUTING.md) for detailed instructions.

## 🔑 License

[MIT](./LICENSE)