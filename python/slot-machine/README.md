# Text-Based Slot Machine

This is a Python project for a text-based slot machine game where users can deposit virtual money, place bets, and try their luck on 1, 2, or 3 lines. The project is designed to demonstrate programming skills such as handling user input, implementing game logic, and managing a balance system. It is intended as part of a portfolio showcasing Python development.

## Features

- **Deposit System:** Users can deposit virtual money into their balance to start playing.
- **Betting Mechanism:** Players can choose to bet on 1, 2, or 3 lines.
- **Win Calculation:** Winning combinations multiply the player's bet by the value of the winning line.
- **Balance Updates:** Winnings are added to the player's balance, and they can continue playing or cash out.
- **Replayability:** Players can decide when to stop and cash out their balance.

## How to Play

1. **Deposit Money:** Enter an amount to deposit into your virtual balance.
2. **Place Your Bet:** Choose how many lines to bet on (1, 2, or 3) and the amount to wager.
3. **Spin the Slot Machine:** The program will determine if you've won and update your balance.
4. **Continue or Cash Out:** You can keep playing or choose to cash out your balance at any time.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```bash
    cd text-based-slot-machine
    ```
3. Run the Python script:
    ```bash
    python slot_machine.py
    ```

## Example Gameplay

```plaintext
Welcome to the Text-Based Slot Machine!
You have deposited $100.
How many lines would you like to bet on? (1, 2, 3): 2
Enter your bet amount: $10

Spinning...
Line 1: 🍒🍒🍒  (Win!)
Line 2: 🛑🍒🍒

Congratulations! You won $30!
Your new balance is $120.

Would you like to play again or cash out? (play/cash out): play
```

## Future Enhancements

- Add more symbols and combinations for higher complexity.
- Implement customizable betting limits.
- Include sound effects for a more engaging experience.
- Add a graphical user interface (GUI).

## Technologies Used

- **Programming Language:** Python

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project is based on a tutorial by [Tech With Tim](https://github.com/techwithtim) and was designed as a beginner-friendly portfolio project to demonstrate Python skills.
