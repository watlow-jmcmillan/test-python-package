from unittest import TestCase
from test import test

class test_tests(TestCase):
    def test_return(self):
        word = "test"
        self.assertEqual(test.return_val(word), word)

    def test_class_return(self):
        word = "test"
        test_class = test.TestClass(word)

        self.assertEqual(test_class.return_word(), word)