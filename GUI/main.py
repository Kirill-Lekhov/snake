class GameGUI:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def draw(self, surface) -> None:
        for element in self.elements:
            draw = getattr(element, "draw", None)

            if callable(draw):
                element.draw(surface)

    def update(self, event) -> None:
        for element in self.elements:
            update = getattr(element, "update", None)

            if callable(update):
                element.update(event)

    def get_state(self) -> list:
        values = []

        for element in self.elements:
            get_state = getattr(element, "get_state", None)

            if callable(get_state):
                values.append(element.get_state())

        return values
