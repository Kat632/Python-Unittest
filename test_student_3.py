import unittest
from student_3 import Student


class TestStudent(unittest.TestCase):
    
    def test_full_name(self):
        student = Student('Griffin', 'Morley-Biggs')

        self.assertEqual(student.full_name, 'Griffin Morley-Biggs')
    
    def test_alert_santa(self):
        student = Student('Griffin', 'Morley-Biggs')
        student.alert_santa()

        self.assertTrue(student.naughty_list)
    
    def test_email(self):
        student = Student('Griffin', 'Morley-Biggs')

        self.assertEqual(student.email, 'griffin.morley-biggs@email.com')


if __name__ == '__main__':
    unittest.main()