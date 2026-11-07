# MOC – The Banker

A simple terminal-based mathematical guessing game written in Python.

## About

MOC – The Banker is a small interactive command-line game where players must solve randomly generated mathematical riddles under time pressure.

You play against MOC, a banker who challenges you with everyday mathematical problems involving objects such as bananas, watches, diamonds and gold coins.

Each correct answer earns you money, while incorrect answers and missed deadlines cost you part of your balance.

Your objective is simple: answer the riddles correctly, manage your money and avoid bankruptcy.

## Features

- Randomly generated mathematical riddles.
- Six mathematical operations: addition, subtraction, multiplication, division, floor division and exponentiation.
- Five rounds per game.
- 15-second time limit for each answer.
- Money management system with rewards and penalties.
- Random objects and numbers to create different questions.
- Animated text displayed directly in the terminal.
- Simple command-line interface.

## Requirements

- Python 3.8 or higher.
- No external libraries required.

## Installation

Clone the repository:

```bash
git clone https://github.com/ARISAADA/MOC-The-Banker.git
```

Navigate to the project directory:

```bash
cd MOC-The-Banker
```

## Usage

Run the game using Python:

```bash
python3 moc.py
```

Follow the instructions displayed in the terminal to start playing.

## Game Rules

- Starting balance: 100 gold coins.
- Correct answer: +20 gold coins.
- Incorrect answer: -10 gold coins.
- Time limit: 15 seconds per question.
- Total rounds: 5.

If your balance reaches zero or below, the game ends immediately.

## Technologies

- Python
- Random module
- Time module
- Select module

## Compatibility

Developed and tested for macOS and Linux.

The current implementation uses Python's `select` module to handle timed terminal input. Windows compatibility is not currently supported.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Created by AriSaada (2026).
