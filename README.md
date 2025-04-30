
# ♟️ Chess AI – Goal-Based Agent Model

An AI-powered Chess Game leveraging the **Minimax algorithm with Alpha-Beta Pruning**, built with Python and visualized using Pygame and HTML/CSS.

---

## 🧠 Overview

This project implements a chess game using **goal-based agents**, a fundamental concept in artificial intelligence. It features an AI opponent capable of making strategic decisions to win, minimize losses, and control the board—making it an ideal application of AI in complex, decision-based environments.

---

## 🔍 Features

- **Goal-Based AI Agent**: Makes decisions based on objectives like checkmating the opponent, capturing pieces, and board control.
- **Minimax Algorithm**: Simulates game states to evaluate the best possible move.
- **Alpha-Beta Pruning**: Optimizes decision-making speed by pruning unnecessary branches in the search tree.
- **Heuristic Evaluation Function**: Scores board states to guide the AI's choices.
- **Turn-Based Play**: Supports human vs AI with proper alternating turns.
- **Web Prototype**: Optional HTML/CSS chessboard layout for UI prototyping.

---

## 🎯 Objectives

- ✅ **Win the game**: Checkmate the opponent’s king.
- ♟️ **Maximize piece advantage**: Capture more opponent pieces while preserving your own.
- 🧠 **Control the board**: Dominate central squares for better positional strength.
- ⚖️ **Avoid stalemates**: Steer clear of draws unless strategically beneficial.
- ⚡ **Optimize moves**: Make efficient and effective decisions using AI algorithms.

---

## 🧰 Tech Stack

| Component     | Usage                                      |
|--------------|--------------------------------------------|
| `Python`     | Core game logic and AI computations        |
| `Pygame`     | Rendering the game interface               |
| `HTML/CSS`   | Chessboard and piece design (prototype UI) |
| `Minimax`    | AI decision-making                         |
| `Alpha-Beta` | Minimax optimization to prune search trees |

---
## 🛠️ Installation Guide

To set up the Chess AI Agent on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Chessai25/Chess-AI-An-Intelligent-Agent-.git
cd Chess-AI-An-Intelligent-Agent-
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Required Dependencies

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```




## ♜ Behind the Code

### 🔁 Minimax Algorithm

- Simulates all possible moves.
- Evaluates positions to select the best one.
- Assumes optimal play from both players (maximizing and minimizing).

### ✂️ Alpha-Beta Pruning

- Skips unnecessary branches.
- Optimizes decision speed and memory usage.

---

## 🔄 Workflow

1. Initialize game state
2. Player makes a move
3. AI evaluates all valid responses
4. AI uses Minimax + Alpha-Beta pruning to decide its move
5. Update board and repeat until checkmate/draw

---

## 📷 Sample Output

![Chessboard Example](https://github.com/user-attachments/assets/7eef944c-0d29-40a2-95ab-deff5fdff84b)

![image](https://github.com/user-attachments/assets/0dd33c6b-3aa4-4e4f-8621-c6d932df2c78)



---


## 👩‍💻 Contributors

- Shweta Datey  
- Archita Raghuwanshi  
- Komal Gongale  
- Gauri Charjan  
- Shreyal Yeole  
- Divya Bhagwat  

---

## 📚 References

- McIlroy-Young, R., et al. (2020). *"Aligning Superhuman AI with Human Behavior: Chess as a Model System."* KDD.
- Knuth, D. E., & Moore, R. W. (1975). *"An Analysis of Alpha-Beta Pruning."* Artificial Intelligence, 6(4), 293–326.

---

## 🏁 Conclusion

This Chess AI demonstrates how intelligent agents can simulate human-like decision-making through strategic algorithms. By focusing on adaptable, goal-oriented behavior, the model proves effective in mastering chess—a benchmark for AI complexity.

---
