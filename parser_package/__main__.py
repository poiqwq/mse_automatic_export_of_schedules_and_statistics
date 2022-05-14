from criterion_package.criterion import FourthCriterion
from parser_package.csv_parser import CsvParser


def main():
    path = '../csv/5383.txt'
    param = FourthCriterion
    file = CsvParser(path)
    file.parse()
    file.apply(param)


if __name__ == "__main__":
    main()


