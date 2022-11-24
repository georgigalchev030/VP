class Processor:
    def __init__(self, name, price, age):
        self.name = name
        self.price = price
        self.age = age

    def print(self):
        print(self.name, self.price, self.age)


class VideoCard(Processor):
    def __init__(self, name, price, age,  vram):
        super().__init__(name, price, age)
        self.vram = vram


cpu = Processor("intel", 457.0, 4)
vcc = VideoCard("nvidia", 560.0, 5, 1232)
cpu.print()
vcc.print()


