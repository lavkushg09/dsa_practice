from collections import defaultdict


class TicTacToe:
    def __init__(self, board_size=3):
        self.n = board_size
        self.count = [defaultdict(int),defaultdict(int)]

        # # Colum_mapping = {
        # #     "0":[0,3],
        # #     "1":[0,4],
        # #     "2":[0,5],
        # #     "3":[1,3],
        # #     "4":[1,4],
        # #     "5":[1,5],
        # #     "6":[2,3],
        # #     "7":[2,4],
        # #     "8":[2,5],
        # # }
        # self.col = {
        #     "0":"3",
        #     "1":"4",
        #     "2":"5"
        # }
    

    def move(self, row, column, player):
        player_info = self.count[player-1]
        print(f"{self.n<<1=}, {self.n << 1 |1 =}")
        player_info[row] +=1
        player_info[self.n+column] +=1

        if row == column:
            player_info[2*self.n] +=1

        if row+column == self.n-1:
            player_info[2*self.n+1] +=1

        possible_win_list = [row, self.n+column, self.n<<1, self.n<<1 | 1 ]
        print(self.count, possible_win_list)
        if any(player_info[count_info] == self.n for count_info in possible_win_list):
            return player
        return 0

def play_example():
    game = TicTacToe(3)

    moves = [
        (0, 0, 1),  # P1
        (0, 2, 2),  # P2
        (1, 1, 1),  # P1
        (0, 1, 2),  # P2
        (2, 2, 1),  # P1 wins on main diagonal
    ]

    for i, (r, c, p) in enumerate(moves, 1):
        result = game.move(r, c, p)
        print(f"Move {i}: Player {p} -> ({r}, {c})")
        print("Player 1 counts:", dict(game.count[0]))
        print("Player 2 counts:", dict(game.count[1]))
        if result != 0:
            print(f"🎉 Player {result} wins!\n")
            break
        print("-" * 30)

if __name__ == "__main__":
    play_example()
        

