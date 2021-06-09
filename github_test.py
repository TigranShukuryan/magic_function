print("jghgv")
class MagicFunction:
    def __init__(self):
        self.sum = 0
    def __call__(self, *args):
        for i in args:
            self.sum += i
        return self.sum

e = MagicFunction()
print(e(20, 30))

