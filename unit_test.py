import unittest

from main import *


class TestOperaciones(unittest.TestCase):
    def setUp(self):
        
        pass

    def test_definitiva(self):
        esperado = 5
        actual = definitiva(5,5,5)
        self.assertEqual(actual, esperado)


    def tearDown(self):

        pass


if __name__ == '__main__':
    unittest.main()