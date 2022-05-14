from parser_package.csv_parser import CsvParser


class Criterion(object):

    def __init__(self, result=None):
        self.result = result

    def check(self, mass):
        pass


class FirstCriterion(Criterion):
    def check(self, mass):
        count = 0
        for i in mass:
            keys = list(i.keys())
            if int(i[keys[2]]) == 5 and int(i[keys[3]]) == 2:
                count += 1
        return count

    def __repr__(self):
        return f"Количество человек, взявших в первом семестре курсовую на 5 и защитивших на 2: {self.result}"


class SecondCriterion(Criterion):
    def check(self, mass):
        count = 0
        for i in mass:
            keys = list(i.keys())
            if int(i[keys[2]]) == 5 and int(i[keys[3]]) == 2 and int(i[keys[4]]) == 5:
                count += 1
        return count

    def __repr__(self):
        return f"Количество человек, которые взяли в первом семестре курсовые на 5 и защитили на 2, " \
               f"во втором семестре выбрали снова на 5: {self.result}"


class ThirdCriterion(Criterion):
    def check(self, mass):
        count = 0
        for i in mass:
            keys = list(i.keys())
            if int(i[keys[2]]) == 5 and int(i[keys[3]]) == 2 and int(i[keys[4]]) == 5 and int(i[keys[5]]) == 5:
                count += 1
        return count

    def __repr__(self):
        return f"Количество человек, которые взяли в первом и втором семестре курсовые на 5, защитили их в первом " \
               f"семестре на 2, а во втором уже на 5: {self.result}"


class FourthCriterion(Criterion):
    def check(self, mass):
        regions = {}
        region = {}
        corr = 0
        for i in mass:
            keys = list(i.keys())
            if len(regions) == 0:
                region = {i[keys[3]]: {"ЕГЭ": [i[keys[2]]], "Успеваемость": [i[keys[4]]]}}
            for j in regions.keys():
                if j == i[keys[3]]:
                    region = {i[keys[3]]: {"ЕГЭ": [regions[j]["ЕГЭ"][0], i[keys[2]]], "Успеваемость": [regions[j]["Успеваемость"][0], i[keys[4]]]}}
                    break
                else:
                    region = {i[keys[3]]: {"ЕГЭ": [i[keys[2]]], "Успеваемость": [i[keys[4]]]}}
            regions.update(region)
        for j in regions.keys():
            x = regions[j]["ЕГЭ"]
            y = regions[j]["Успеваемость"]
            if len(x) > 1:
                n = len(x)
                sum_x = float(sum(x))
                sum_y = float(sum(y))
                sum_x_sq = sum(xi * xi for xi in x)
                sum_y_sq = sum(yi * yi for yi in y)
                psum = sum(xi * yi for xi, yi in zip(x, y))
                num = psum - (sum_x * sum_y / n)
                den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
                if den == 0:
                    corr = 0
                else:
                    corr = num / den
        return corr


class AllCriterion:
    @staticmethod
    def check(path_to_csv):
        criteria = FirstCriterion, SecondCriterion, ThirdCriterion
        parser = CsvParser(path_to_csv)
        parser.parse()
        criteria = [criterion(parser.apply(criterion)) for criterion in criteria]
        [print(criterion) for criterion in criteria]

