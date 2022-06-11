class MyClass:
    def __init__(self):
        self.x = 2

    def get_x(self):
        return self.x


class MyClassNoSelf:
    def __init__():
        x = 6

    def get_x():
        return x


with_self = MyClass()
with_self_x = with_self.get_x()
print(with_self_x)

no_self = MyClassNoSelf()
no_self_x = no_self.get_x()
print(no_self_x)

