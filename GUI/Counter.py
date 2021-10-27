from pygame import Color

from .label import Label


class Counter(Label):
    def __init__(self, label_rect: tuple, event_for_update, bgcolor=Color("white"), font_color: Color = Color("black"),
                 start_value: int = 0):
        super().__init__(label_rect, str(start_value), bgcolor, font_color)

        self.event_for_update = event_for_update
        self.value = start_value

    def update(self, event):
        if event.type == self.event_for_update:
            self.value += 1
            self.text = str(self.value)

    def get_state(self) -> int:
        return self.value
