class TestCase:

    def __init__(self, name):
        self.name = name

    def Run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):

    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1


test = WasRun("testMethod")
print(test.wasRun)
test.Run()
print(test.wasRun)
