class GUI:
    def __init__(self, num):
        self.elements = []
        self.nums = {}
        self.num = num

    def add_element(self, element, num):
        self.elements.append(element)
        self.nums[element] = num

    def render(self, surface):
        for element in self.elements:
            if self.nums[element] == self.num:
                render = getattr(element, "render", None)

                if callable(render):
                    element.render(surface)

    def update(self):
        for element in self.elements:
            update = getattr(element, "update", None)

            if callable(update):
                element.update()

    def get_event(self, event):
        for element in self.elements:
            get_event = getattr(element, "get_event", None)

            if callable(get_event):
                element.get_event(event)

    def smena(self, num):
        self.num = num

    def get_num(self):
        return self.num
