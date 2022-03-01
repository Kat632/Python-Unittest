import unittest
from student_5 import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('set up')
        self.student = Student('Griffin', 'Morley-Biggs')
    
    def tearDown(self):
        print('tear down')
    
    def test_full_name(self):
        print('test full name')

        self.assertEqual(self.student.full_name, 'Griffin Morley-Biggs')
    
    def test_alert_santa(self):
        print('test alert santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)
    
    def test_email(self):
        print('test email')
        self.assertEqual(self.student.email, 'griffin.morley-biggs@email.com')
    
    def test_apply_extension(self):
        print('test apply extension')
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


if __name__ == '__main__':
    unittest.main()