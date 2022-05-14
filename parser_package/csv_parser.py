import pandas


class CsvParser(object):

    def __init__(self, path_to_csv):
        self._path = path_to_csv
        self._content = []

    # Parsing csv into list of dict
    def parse(self):
        df = pandas.read_csv(self._path, delimiter=';')
        content = df.to_dict('records')
        for i in content:
            self._content.append(i)
        return self._content

    # Apply criterion_package
    def apply(self, param):
        applied = param()
        count = applied.check(self._content)
        return count
