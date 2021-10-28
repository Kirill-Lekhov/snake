from pygame import Color

from constants import TIMER_UPDATE
from .label import Label


class Stopwatch(Label):
    def __init__(self, label_rect: tuple, bgcolor=Color("white"), font_color: Color = Color("black")):
        super().__init__(label_rect, "00:00", bgcolor, font_color)
        self.seconds = 0

    def update(self, event) -> None:
        if event.type == TIMER_UPDATE:
            self.seconds += 1
            self.text = self.convert_time()

    def convert_time(self) -> str:
        minutes = self.seconds // 60
        seconds = self.seconds % 60

        return f"{minutes:02}:{seconds:02}"

    def get_state(self) -> str:
        return self.convert_time()
