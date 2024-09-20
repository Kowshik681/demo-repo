import unittest
def multiply(a,b):
    return a * b
class MultiplyTestcase(unittest.TestCase):
    def test_1(self):
        result = multiply(3,4)
        self.assertequal(result,12)
        def test_2(self):
            result = multiply(3,-4)
            self.assertequal(result,-12)
        def test_3(self):
            result = multiply(-3,-4)
            self.assertequal(result,12)
        def test_4(self):
            result = multiply(3,0)
            self.assertequal(result,0)
        def test_5(self):
            result = multiply(3,0)
            self.assertequal(result,0)
        def test_6(self):
            result = multiply(3,1)
            self.assertequal(result,3)
if __name__ == '__main__':
    unittest.main()
        
