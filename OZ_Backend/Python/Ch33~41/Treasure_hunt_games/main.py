import random
import math
import os


class Treasure:
    def __init__(self, board_size):
        self.board_size = board_size
        self.treasure_position = None
        self.player_position = None
        self.player_count = 0
        self.game_board = self.initialize_game()

    def initialize_game(self):
        print("Hello Explorer\n")
        game_board = [
            [0 for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        self.treasure_position = (
            random.randint(0, self.board_size - 1),
            random.randint(0, self.board_size - 1),
        )
        game_board[self.treasure_position[0]][self.treasure_position[1]] = "T"
        place_bool = False
        while not place_bool:
            self.player_position = (
                random.randint(0, self.board_size - 1),
                random.randint(0, self.board_size - 1),
            )
            if self.player_position != self.treasure_position:
                game_board[self.player_position[0]][self.player_position[1]] = "Y"
                place_bool = True
        return game_board

    def update_board(self, player_position):
        self.game_board[player_position[0]][player_position[1]] = "Y"

    def calculate_distance(self, player_position) -> float:
        x1, y1 = self.treasure_position
        x2, y2 = player_position

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    # 화면에 표시되는 방향에 맞춰 x, y 2차원 위치를 조정했습니다.
    def move_player(self, direction):
        new_x, new_y = self.player_position
        if direction == "D":  # 오른쪽
            new_y += 1
            if new_y >= self.board_size:
                self.block_road()
                new_y = self.board_size - 1  # 가장 오른쪽 끝까지 이동
        elif direction == "A":  # 왼쪽
            new_y -= 1
            if new_y < 0:
                self.block_road()
                new_y = 0  # 가장 왼쪽 끝까지 이동
        elif direction == "W":  # 위로
            new_x -= 1
            if new_x < 0:
                self.block_road()
                new_x = 0  # 가장 위 끝까지 이동
        elif direction == "S":  # 아래
            new_x += 1
            if new_x >= self.board_size:
                self.block_road()
                new_x = self.board_size - 1  # 가장 아래 끝까지 이동
        else:
            raise ValueError(
                "유효하지 않은 방향입니다. 'D', 'A', 'W', 'S' 중에서 선택하세요."
            )
        self.game_board[self.player_position[0]][self.player_position[1]] = 0
        self.player_position = (new_x, new_y)
        return self.player_position

    def block_road(self) -> None:
        print("막혔습니다. 다른 방향으로 가세요 ~ \n")

    def play_game(self):

        while True:
            try:
                print("현재 위치!\n================================\n")
                for _ in self.game_board:
                    print(_)
                print("\n=====================\n")
                direction = input("방향키 : ")
                print("\n=====================\n")
                self.player_count += 1
                a = self.move_player(direction)

                self.update_board(a)

                if self.player_position == self.treasure_position:
                    self.game_board[self.player_position[0]][
                        self.player_position[1]
                    ] = "Find!!!"
                    print("보물 찾았습니다!\n")
                    print(f"총 이동 횟수 : {self.player_count}\n")
                    for _ in self.game_board:
                        print(_)
                    break
                else:
                    distance = self.calculate_distance(a)
                    print(f"보물과의 거리: {distance:.2f}")

            except ValueError as e:
                print(e)

            # os.system("cls")


# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    board_size = 5  # 보드 크기를 5x5로 설정
    treasure = Treasure(board_size)
    treasure.play_game()
