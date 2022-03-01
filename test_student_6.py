import unittest
from student_6 import Student
from datetime import timedelta
from unittest.mock import patch


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
    
    def test_course_schedule_success(self):
        print('test course schedule')
        with patch("student_6.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
        
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        print('test course schedule failed')
        with patch("student_6.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
        
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")

if __name__ == '__main__':
    unittest.main()