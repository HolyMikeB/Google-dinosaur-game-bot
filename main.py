import pyautogui


class Dinosaur:

    def __init__(self):
        self.jumps = 0

    def jump(self):
        pyautogui.keyDown('up')
        pyautogui.sleep(.2)
        pyautogui.keyUp('up')
        self.jumps += 1

    def cactus_ahead(self) -> bool:
        x = 1060 + int(self.jumps * .3)
        pixel = pyautogui.pixel(x, 430)
        for color in pixel:
            if color < 100:
                return True
        return False

    def game_over(self) -> bool:
        pixel = pyautogui.pixel(1195, 362)
        for color in pixel:
            if color < 100:
                return True
        return False


def main():
    dino = Dinosaur()
    playing = True

    while playing:
        if dino.cactus_ahead():
            dino.jump()

        if dino.game_over():
            play_again = input('Do you want to play again? Y/N ').lower()
            if play_again == 'n':
                playing = False
            else:
                pyautogui.click(1282, 404)


if __name__ == '__main__':
    main()



