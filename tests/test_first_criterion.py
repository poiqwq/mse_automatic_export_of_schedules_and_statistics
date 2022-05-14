import unittest
from parser_package.csv_parser import CsvParser
from criterion_package.criterion import FirstCriterion


class TestFirstCriterion(unittest.TestCase):
  def setUp(self):
    self.file1 = CsvParser('../csv/3381.txt')
    self.file2 = CsvParser('../csv/3382.txt')
    self.file3 = CsvParser('../csv/3383.txt')
    self.file4 = CsvParser('../csv/3384.txt')
    self.file5 = CsvParser('../csv/3301.txt')

  def test_3381(self):
    self.file1.parse()
    self.assertEqual(self.file1.apply(FirstCriterion), 2)

  def test_3382(self):
    self.file2.parse()
    self.assertEqual(self.file2.apply(FirstCriterion), 0)

  def test_3383(self):
    self.file3.parse()
    self.assertEqual(self.file3.apply(FirstCriterion), 11)

  def test_3384(self):
    self.file4.parse()
    self.assertEqual(self.file4.apply(FirstCriterion), 3)

  def test_3301(self):
    self.file5.parse()
    self.assertEqual(self.file5.apply(FirstCriterion), 2)


if __name__ == "__main__":
  unittest.main()
