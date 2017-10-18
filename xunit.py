class WasRun:
    def __init__(self,name):
        self.wasRun = None
    def Run(self):
        self.testMethod()
    def testMethod(self):
        self.wasRun = 1

test = WasRun("testMethod")
print(test.wasRun)
test.Run()
print(test.wasRun)

