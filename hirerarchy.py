class Bird:
    def fly(self):
        print("I can fly")

class Parrot(Bird):
    def sing(self):
        print("I can sing dododoodod")

class Eagle(Bird):
    def vision(self):
        print("I can see everything ..")
class Penguin(Bird):
    def swim(self):
        print("I can swim yoooooooo")

pa = Parrot()
ea = Eagle()
pen = Penguin()

pa.fly()
pa.sing()

ea.fly()
ea.vision()

pen.fly()
pen.swim()
