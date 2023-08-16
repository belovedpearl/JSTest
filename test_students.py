import unittest
from student import Student


class TestStudents(unittest.TestCase):
    def test_full_name(self):
        student = Student("John", "Doe")        # create an instance of the class
        self.assertEqual(student.full_name, "John Doe")

if __name__ == "__main__":
    unittest.main()