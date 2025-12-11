import unittest
from all import highest_grade, lowest_grade, most, avg


grades = [50, 60, 66, 60, 88, 99, 3, 10, 14, 13.3]
print("Grades:", grades)


class TestsNStuff(unittest.TestCase):
    def test_highest(self):
        self.assertEqual(highest_grade(grades), 99)

    def test_lowest(self):
        self.assertEqual(lowest_grade(grades), 3)

    def test_avg(self):
        self.assertEqual(avg(grades), 46.3)

    def test_most(self):
        self.assertEqual(most(grades), 60)


if __name__ == "__main__":
    unittest.main()
