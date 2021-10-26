from pygame import Color, Rect
from pygame.font import Font


class Label:
    def __init__(self, label_rect: tuple, text: str, bgcolor=Color("white"), font_color: Color = Color("black")):
        self.rect = Rect(label_rect)
        self.text = text
        self.bgcolor = bgcolor
        self.font_color = font_color

        # Рассчитываем размер шрифта в зависимости от высоты
        self.font = Font(None, self.rect.height - 4)
        self.rendered_text = None
        self.rendered_rect = None

    def _change_text(self, new_text) -> None:
        self.text = new_text

    def draw(self, surface) -> None:
        if self.bgcolor != -1:
            surface.fill(self.bgcolor, self.rect)

        self.rendered_text = self.font.render(self.text, 1, self.font_color)
        self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 2, centery=self.rect.centery)
        
        # выводим текст
        surface.blit(self.rendered_text, self.rendered_rect)
