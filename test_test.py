import test

class Testtest(unittest.TestCase):

    def setUp(self):
        self.hello_message = "Hello, test!"

    def test_prints_hello_test(self):
        output = test.hello()
        assert(output == self.hello_message)
