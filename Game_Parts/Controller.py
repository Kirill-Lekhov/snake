from pygame import K_w, K_UP, K_d, K_RIGHT, K_s, K_DOWN, K_a, K_LEFT, KEYDOWN, KEYUP


class Controller:
    WASD = K_w, K_d, K_s, K_a
    ARROWS = K_UP, K_RIGHT, K_DOWN, K_LEFT

    def __init__(self, use_arrows: bool = True, use_wasd: bool = True):
        self.controls = {"up": [], "right": [], "down": [], "left": []}

        if use_wasd:
            self.set_controls(self.WASD)

        if use_arrows:
            self.set_controls(self.ARROWS)

    def set_controls(self, buttons: tuple) -> None:
        for key_number, key in enumerate(self.controls):
            self.controls[key].append(buttons[key_number])

    def process_event(self, event) -> str:
        move_direction = None

        if event.type == KEYDOWN:
            for key, value in self.controls.items():
                if event.key in value:
                    move_direction = key

        return move_direction
