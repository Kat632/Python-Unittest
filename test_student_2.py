import unittest
from student_2 import Student


class TestStudent(unittest.TestCase):
    
    def test_full_name(self):
        student = Student('Griffin', 'Morley-Biggs')

        self.assertEqual(student.full_name, 'Griffin Morley-Biggs')
    
    def test_alert_santa(self):
        student = Student('Griffin', 'Morley-Biggs')
        student.alert_santa()

        self.assertTrue(student.naughty_list)


if __name__ == '__main__':
    unittest.main()