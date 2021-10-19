from pygame import Color, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.draw import rect, line

from .Label import Label


class Button(Label):
    def __init__(self, rect, text, color, num,surface):
        super().__init__(rect, text)
        self.bgcolor = color

        # при создании кнопка не нажата
        self.pressed = False
        self.number = num
        self.surface = surface

    def render(self, surface):
        surface.fill(self.bgcolor, self.rect)
        self.rendered_text = self.font.render(self.text, 1, self.font_color)

        if not self.pressed:
            color1 = Color("white")
            color2 = Color("black")
            self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 5, centery=self.rect.centery)

        else:
            color1 = Color("black")
            color2 = Color("white")
            self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 7, centery=self.rect.centery + 2)

        # рисуем границу
        rect(surface, color1, self.rect, 2)
        line(surface, color2, (self.rect.right - 1, self.rect.top), (self.rect.right - 1, self.rect.bottom), 2)
        line(surface, color2, (self.rect.left, self.rect.bottom - 1),
                         (self.rect.right, self.rect.bottom - 1), 2)

        # выводим текст
        surface.blit(self.rendered_text, self.rendered_rect)

    def get_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.pressed = self.rect.collidepoint(event.pos)

        elif event.type == MOUSEBUTTONUP and event.button == 1:
            # gui.smena(1)
            pass
