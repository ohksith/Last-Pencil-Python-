# Last Pencil

---

## Description

This program simulates a game involving a certain number of pencils placed on a table between two players. The game has specific rules determining the winning and losing positions based on the number of pencils present. The objective is to implement a bot that follows a winning strategy to play against a human player.

### Game Rules

The game is played with the following rules:

- If there are 2, 3, or 4 pencils on the table, the current player wins by following a specific strategy.
- If there are 5 pencils on the table, the current player loses regardless of their move.
- If there are 6, 7, or 8 pencils on the table, the game repeats its pattern.
- Players take turns removing 1, 2, or 3 pencils from the table.
- The goal is to force the opponent to take the last remaining pencil, leading to their loss.

### Bot Logic

The bot follows specific strategies based on its winning or losing position:

- If the bot is in a losing position (5, 9, 13, 17... pencils), it takes a random number of pencils (1 to 3) or the last pencil if only one is left.
- If the bot is in a winning position, it aims to force the opponent into a losing position:
  - With 4, 8, 12, 16... pencils, the bot takes 3 pencils.
  - With 3, 7, 11, 15... pencils, the bot takes 2 pencils.
  - With 2, 6, 10, 14... pencils, the bot takes 1 pencil.

### Objectives

- Implement the bot for the second player.
- Expand the program to handle any initial number of pencils.
- On the bot's turn, output its move following the winning strategy. If the bot is not in a winning position, use any pattern for its move.

### Examples

Example 1:

```
How many pencils would you like to use:
> 10
Who will be the first (John, Jack):
> Jack
||||||||||
Jack's turn:
1
|||||||||
John's turn!
> 2
|||||||
Jack's turn:
2
|||||
John's turn!
> 1
||||
Jack's turn:
3
|
John's turn!
> 1
Jack won!
```

Example 2:

```
How many pencils would you like to use:
> 6
Who will be the first (John, Jack):
> John
||||||
John's turn!
> 1
|||||
Jack's turn:
2
|||
John's turn!
> 2
|
Jack's turn:
1
John won!
```
