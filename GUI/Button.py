from pygame import Color, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.draw import rect, line
from pygame.event import Event

from .Label import Label


class Button(Label):
    def __init__(self, button_rect, text, event, pygame, bgcolor=Color("white"), font_color: Color = Color("black")):
        super().__init__(button_rect, text, bgcolor, font_color)
        self.pressed = False
        self.event = Event(event)
        self.post_event = pygame.event.post

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.pressed = self.rect.collidepoint(event.pos)

        elif event.type == MOUSEBUTTONUP and event.button == 1:
            if self.pressed:
                self.post_event(self.event)

            self.pressed = False

    def draw(self, surface):
        if self.bgcolor != -1:
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
        line(surface, color2, (self.rect.left, self.rect.bottom - 1), (self.rect.right, self.rect.bottom - 1), 2)

        # выводим текст
        surface.blit(self.rendered_text, self.rendered_rect)
