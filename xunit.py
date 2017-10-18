class WasRun:

    def __init__(self, name):
        self.wasRun = None
        self.name = name

    def Run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = 1


test = WasRun("testMethod")
print(test.wasRun)
test.Run()
print(test.wasRun)
