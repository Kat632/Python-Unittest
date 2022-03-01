import unittest
from student import Student


class TestStudent(unittest.TestCase):
    
    def test_full_name(self):
        student = Student('Griffin', 'Morley-Biggs')


if __name__ == '__main__':
    unittest.main()