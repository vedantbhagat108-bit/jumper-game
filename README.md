# Maria's Mushroom Run

**Maria's Mushroom Run** is a 2D side-scrolling platformer game built using **Python** and **Pygame**.
The game features player movement, double jump, enemies, collectibles, sound effects, a pause menu, and level completion .

This project was built as a beginner-friendly portfolio project to demonstrate Python programming, game development basics, file handling, and modular code structure.

---

## Features

* 2D side-scrolling platformer gameplay
* Player movement with double jump
* Collectible mushrooms
* Enemy collision and enemy defeat system
* Lives and score system
* Pause menu
* Game over screen
* Level complete screen
* Background music and sound effects
* Modular project structure

---

## Tech Stack

* Python
* Pygame
* Git and GitHub for version control

---

## Project Structure

```txt
maria-mushroom-run/
│
├── assets/
│   ├── images/
│   │   ├── background.png
│   │   ├── maria.png
│   │   ├── mushroom.png
│   │   ├── enemy.png
│   │   ├── platform.png
│   │   ├── castle.png
│   │   └── flagpole.png
│   │
│   └── sounds/
│       ├── jump.wav
│       ├── coin.wav
│       ├── hit.wav
│       ├── win.wav
│       └── music.mp3
│
├── src/
│   ├── main.py
│   ├── settings.py
│   ├── player.py
│   ├── sprites.py
│   ├── ui.py
│   ├── assets.py
|
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## How to Run the Game

### 1. Clone the repository

```bash
git clone https://github.com/your-username/maria-mushroom-run.git
```

### 2. Open the project folder

```bash
cd maria-mushroom-run
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the game

```bash
python src/main.py
```

---

## Controls

| Key         | Action                  |
| ----------- | ----------------------- |
| Left Arrow  | Move Left               |
| Right Arrow | Move Right              |
| Space       | Jump / Double Jump      |
| ESC         | Pause / Resume          |
| R           | Restart from Pause Menu |
| Q           | Quit from Pause Menu    |

---

## Gameplay

The player controls Maria and moves through a side-scrolling level.
The objective is to collect mushrooms, avoid or defeat enemies, and reach the flagpole near the castle to complete the level.

The game includes:

* Mushrooms for score
* Enemies that reduce lives on collision
* Double jump for better movement

---

## What I Learned

While building this project, I learned:

* How to create a game loop using Pygame
* How to handle keyboard input
* How to use sprites and sprite groups
* How to implement collision detection
* How to add sound effects and background music
* How to organize code into multiple files
* How to use Git and GitHub for version control

---

## Future Improvements

* Add multiple levels
* Add animated sprites
* Add a main menu with buttons
* Add moving platforms
* Add power-ups
* Add a boss level
* Package the game as a Windows executable

---

## Author

**Vedant Bhagat**

B.Tech Information Technology
Delhi Technological University

---

## Note

This project is created for learning and portfolio purposes.
