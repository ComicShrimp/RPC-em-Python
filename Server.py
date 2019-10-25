import rpyc
from rpyc.utils.server import ThreadedServer

class CalculatorService(rpyc.Service):
    def exposed_add(self, a, b):
        return a + b

    def exposed_sub(self, a, b):
        return a - b

    def exposed_mul(self, a, b):
        return a * b

    def exposed_div(self, a, b):
        return a / b

    def foo(self):
        print ("foo")

thread = ThreadedServer(CalculatorService, port=35000)
thread.start()