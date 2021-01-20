import unittest

class TestMyProgram(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'Foo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
if __name__ == '__main__':
    unittest.main()