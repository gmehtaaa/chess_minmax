# Chess AI using Minimax with Alpha-Beta Pruning

## Problem Statement
This project implements a Chess AI that plays optimally using the **Minimax algorithm with Alpha-Beta pruning**.  
The game follows standard Chess rules with the following setup:
- The board is an 8×8 grid.
- The player chooses whether to play as White (X) or Black (O).
- The computer AI uses minimax with alpha-beta pruning to select the best possible move.
- The AI plays optimally and aims to avoid losing.

---

## Time & Space Complexity

### Time Complexity
- Without pruning: **O(b^d)**
  - `b` = branching factor (average ~35 moves in chess).
  - `d` = depth of the search tree (chosen depth, e.g., 3–4).
  - Complexity grows exponentially with depth.
- With Alpha-Beta pruning:
  - Reduces the effective branching factor.
  - Best case: **O(b^(d/2))**.
  - Practically, pruning allows deeper searches within the same time.

### Space Complexity
- **O(d)** due to recursion stack depth, where `d` is search depth.
- Each recursive call stores the board state temporarily.
- Memory usage is manageable because only one branch of the game tree is stored at a time.

---

## Use Cases
- Demonstrates **Minimax + Alpha-Beta pruning** in a real-world complex game (Chess).
- Educational tool to explain:
  - **Game Tree Search**
  - **Pruning Techniques** to optimize performance.
- Can be extended with:
  - Positional evaluation heuristics.
  - Deeper search with iterative deepening.
  - Opening books and endgame tables.

---

## Learning Outcomes
- Understand the concept of **adversarial search** in AI.
- Learn how **alpha-beta pruning** reduces unnecessary computation in minimax.
- Gain hands-on experience with recursion, backtracking, and decision-making in uncertain environments.
- Appreciate the computational challenges of Chess compared to simpler games like Tic-Tac-Toe.
- Build intuition for how real-world game engines balance **search depth** and **heuristic evaluations**.

---
