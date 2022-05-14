import unittest
from parser_package.csv_parser import CsvParser
from criterion_package.criterion import ThirdCriterion


class TestThirdCriterion(unittest.TestCase):
    def setUp(self):
        self.file1 = CsvParser('../csv/1301.txt')
        self.file2 = CsvParser('../csv/1381.txt')
        self.file3 = CsvParser('../csv/1382.txt')
        self.file4 = CsvParser('../csv/1383.txt')
        self.file5 = CsvParser('../csv/1384.txt')

    def test_1301(self):
        self.file1.parse()
        self.assertEqual(self.file1.apply(ThirdCriterion), 2)

    def test_1381(self):
        self.file2.parse()
        self.assertEqual(self.file2.apply(ThirdCriterion), 3)

    def test_1382(self):
        self.file3.parse()
        self.assertEqual(self.file3.apply(ThirdCriterion), 0)

    def test_1383(self):
        self.file4.parse()
        self.assertEqual(self.file4.apply(ThirdCriterion), 5)

    def test_1384(self):
        self.file5.parse()
        self.assertEqual(self.file5.apply(ThirdCriterion), 6)


if __name__ == "__main__":
    unittest.main()
