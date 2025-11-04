problem = "problem5"
student_name = "nour"
student_number = "t0326796"

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time
import matplotlib

matplotlib.use("TkAgg")  # Tkinter is used for GUI

def basic_knights_tour():
    # provided the horizontal and vertical arrays represent the 8 possible moves 
    horizontal = [2, 1, -1, -2, -2, -1, 1, 2]
    vertical = [-1, -2, -2, -1, 1, 2, 2, 1]

    # define possible knight moves
    MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # 8x8 chessboard
    def generate_board():
        return np.zeros((8, 8), dtype=int)

    # checks if a move is valid 
    def is_valid_move(x, y, board):
        return 0 <= x < 8 and 0 <= y < 8 and board[x, y] == 0

    def get_valid_moves(x, y, board):
        valid_moves = []
        for i in range(8):
            new_x = x + vertical[i]
            new_y = y + horizontal[i]
            if is_valid_move(new_x, new_y, board):
                valid_moves.append((new_x, new_y))
        return valid_moves

    # main class to run the game
    class KnightsTourGame:
        def __init__(self, mode="interactive"):
            self.mode = mode
            self.board = generate_board()
            self.x, self.y = 4, 3
            self.board[self.x, self.y] = 1
            self.step = 2
            self.fig, self.ax = plt.subplots(figsize=(6, 6))
            self.fig.canvas.mpl_connect("button_press_event", self.on_click)
            self.update_board()

            # automatic mode 
            if self.mode == "automatic":
                plt.ion()  # enable interactive mode
                self.run_automatic_tour()
                plt.ioff()  # restore normal behavior

            # show GUI for both modes safely
            plt.show()

        # updates the visualisation 
        def update_board(self):
            self.ax.clear()
            chessboard = np.zeros((8, 8))
            ## set colours for the squares
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        chessboard[i, j] = 1

            sns.heatmap(chessboard, cmap=["#DDB88C", "#A67B5B"], cbar=False, linewidths=0.3, linecolor="black", ax=self.ax)

            # show the number where the knight has moved
            for i in range(8):
                for j in range(8):
                    if self.board[i, j] > 0:
                        self.ax.text(j + 0.1, i + 0.2, str(int(self.board[i, j])), 
                                     ha='left', va='top', fontsize=10, color='black', fontweight='bold')

            # highlights valid next move 
            valid_moves = get_valid_moves(self.x, self.y, self.board)
            for move in valid_moves:
                self.ax.text(move[1] + 0.5, move[0] + 0.5, 'X', ha='center', va='center', 
                             fontsize=18, color='red', fontweight='bold')

            # displays current knight position 
            self.ax.text(self.y + 0.5, self.x + 0.5, '♞', ha='center', va='center', 
                         fontsize=18, color='black', fontweight='bold')

            self.ax.set_xticks(np.arange(8) + 0.5)
            self.ax.set_yticks(np.arange(8) + 0.5)
            self.ax.set_xticklabels(np.arange(8))
            self.ax.set_yticklabels(np.arange(8))
            self.ax.invert_yaxis()
            self.ax.set_title("Click on a valid move to play" if self.mode == "interactive" else "Automatic Mode Running...")
            plt.draw()
            plt.pause(0.001)  # important to force redraw in automatic mode

            # end game if 64 moves done or no more moves available 
            if self.step > 64 or not get_valid_moves(self.x, self.y, self.board):
                self.ax.set_title(f"Game Over! Total moves: {self.step - 1}")
                plt.draw()

        # handle clicks for interactive mode 
        def on_click(self, event):
            if self.mode == "automatic":
                return

            col, row = int(event.xdata), int(event.ydata)
            valid_moves = get_valid_moves(self.x, self.y, self.board)

            if (row, col) in valid_moves:
                self.x, self.y = row, col
                self.board[self.x, self.y] = self.step
                self.step += 1
                self.update_board()
            else:
                print("Invalid move! Click on a red X.")

        # automatic mode 
        def run_automatic_tour(self):
            print("Automatic tour started!")
            while self.step <= 64:
                valid_moves = get_valid_moves(self.x, self.y, self.board)
                if not valid_moves:
                    break

                chosen_move = random.choice(valid_moves)
                self.x, self.y = chosen_move
                self.board[self.x, self.y] = self.step
                self.step += 1
                self.update_board()
                time.sleep(0.5)

            print(f"Automatic mode finished after {self.step - 1} moves.")

    # brute force method 
    def brute_force_knights_tour(num_trials=1000000):
        moves_completed = []
        completed_tours = 0
        selected_tours = []

        for trial in range(num_trials):
            board = generate_board()
            x, y, step = 4, 3, 1
            board[x, y] = step
            tour_path = [(x, y)]
            step += 1

            while step <= 64:
                valid_moves = get_valid_moves(x, y, board)
                if not valid_moves:
                    break
                x, y = random.choice(valid_moves)
                board[x, y] = step
                tour_path.append((x, y))
                step += 1

            moves_completed.append(step - 1)
            if step - 1 == 64:
                completed_tours += 1
                if len(selected_tours) < 5:
                    selected_tours.append(tour_path)

            if (trial + 1) % 10000 == 0:
                print(f"{trial + 1} trials completed...")

        print(f"Completed tours: {completed_tours} out of {num_trials} ({(completed_tours/num_trials)*100:.2f}%)")
        plt.figure(figsize=(10,6))
        sns.histplot(moves_completed, bins=64, kde=False)
        plt.title('Distribution of Moves Completed (Brute Force)')
        plt.xlabel('Number of Moves Completed')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

        for idx, tour in enumerate(selected_tours):
            board = np.zeros((8, 8))
            for step_num, (x, y) in enumerate(tour, start=1):
                board[x, y] = step_num
            plt.figure(figsize=(5, 5))
            sns.heatmap(board, annot=True, fmt=".0f", cmap="YlGnBu", cbar=False, linewidths=0.5, linecolor='black')
            plt.title(f"Brute Force Completed Tour #{idx+1}")
            plt.xticks(np.arange(8)+0.5, labels=np.arange(8))
            plt.yticks(np.arange(8)+0.5, labels=np.arange(8))
            plt.gca().invert_yaxis()
            plt.show()

    # heuristic based approach 
    def heuristic_knights_tour(num_trials=1000000):
        moves_completed = []
        completed_tours = 0
        selected_tours = []

        for trial in range(num_trials):
            board = generate_board()
            x, y, step = 4, 3, 1
            board[x, y] = step
            tour_path = [(x, y)]
            step += 1

            while step <= 64:
                valid_moves = get_valid_moves(x, y, board)
                if not valid_moves:
                    break

                move_scores = []
                for move in valid_moves:
                    onward_moves = len(get_valid_moves(move[0], move[1], board))
                    move_scores.append((onward_moves, move))

                min_onward = min(move_scores)[0]
                candidates = [move for score, move in move_scores if score == min_onward]
                x, y = random.choice(candidates)
                board[x, y] = step
                tour_path.append((x, y))
                step += 1

            moves_completed.append(step - 1)
            if step - 1 == 64:
                completed_tours += 1
                if len(selected_tours) < 5:
                    selected_tours.append(tour_path)

            if (trial + 1) % 10000 == 0:
                print(f"{trial + 1} heuristic trials completed...")

        print(f"[Heuristic] Completed tours: {completed_tours} out of {num_trials} ({(completed_tours/num_trials)*100:.2f}%)")
        plt.figure(figsize=(10,6))
        sns.histplot(moves_completed, bins=64, kde=False)
        plt.title('Distribution of Moves Completed (Heuristic)')
        plt.xlabel('Number of Moves Completed')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

        for idx, tour in enumerate(selected_tours):
            board = np.zeros((8, 8))
            for step_num, (x, y) in enumerate(tour, start=1):
                board[x, y] = step_num
            plt.figure(figsize=(5, 5))
            sns.heatmap(board, annot=True, fmt=".0f", cmap="YlOrBr", cbar=False, linewidths=0.5, linecolor='black')
            plt.title(f"Heuristic Completed Tour #{idx+1}")
            plt.xticks(np.arange(8)+0.5, labels=np.arange(8))
            plt.yticks(np.arange(8)+0.5, labels=np.arange(8))
            plt.gca().invert_yaxis()
            plt.show()

    # run everything
    mode = input("Choose mode: 'interactive' or 'automatic': ").strip().lower()
    while mode not in ["interactive", "automatic"]:
        mode = input("Invalid choice. Enter 'interactive' or 'automatic': ").strip().lower()

    # run KnightsTourGame in the main thread (safe for GUI)
    KnightsTourGame(mode)

    # then run simulations
    brute_force_knights_tour()
    heuristic_knights_tour()

basic_knights_tour()
