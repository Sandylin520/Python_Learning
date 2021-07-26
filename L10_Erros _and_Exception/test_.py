import unittest
import cap


# When this lowercase python gets passed into the text function,
# that it always returns back the capitalized P version of Python.
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,"Python")

    def test_multiple_words(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')
#   File "c:\Python learning\L10_Erros _and_Exception\test_.py", line 16
#     self.assertEqual(result,'Monty Python')
#     ^
#   SyntaxError: invalid syntax

if __name__=='__main__':
    #The main() function of unittest is what execute all tests.
    unittest.main()

#you'll need to use certain words at your function name, to be tested.
#That's why we create a function that uses our function to be tested.
#If we pass the name cap directly, it wouldn't be tested.