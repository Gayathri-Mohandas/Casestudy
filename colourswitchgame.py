import random

class ColorSwitchGame:
    def __init__(self):
        self.player_color = self.get_random_color()
        self.obstacle_color = self.get_random_color()
        self.score = 0

    def get_random_color(self):
        colors = ["Red", "Blue", "Green", "Yellow"]
        return random.choice(colors)

    def display_info(self):
        print(f"Player Color: {self.player_color}")
        print(f"Obstacle Color: {self.obstacle_color}")
        print(f"Score: {self.score}")

    def play_round(self):
        self.display_info()

        if self.player_color == self.obstacle_color:
            print("Game Over!")
            print(f"Your final score: {self.score}")
            return False

        print("Jump! (Press any key)")
        input()

        self.player_color = self.obstacle_color
        self.obstacle_color = self.get_random_color()
        self.score += 1

        return True

def main():
    print("Color Switch Game")

    game = ColorSwitchGame()
    while game.play_round():
        pass

if __name__ == "__main__":
    main()
