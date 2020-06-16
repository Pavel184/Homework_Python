# Pavel Krupenya
# Cars
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Start drawing")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f"Start drawing by {self.title}\n")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f"Start drawing by {self.title}\n")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f"Start drawing by {self.title}\n")

pen = Pen("Pen")
pen.draw()

pencil = Pencil("Pencil")
pencil.draw()

handle = Handle("Handle")
handle.draw()

input("\nPress Enter for exit")