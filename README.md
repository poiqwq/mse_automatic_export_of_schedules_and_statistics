#### CsvParser и Criterion (FirstCriterion, SecondCriterion, ThirdCriterion, FourthCriterion)
Использование классов:
1. Создать экземпляр класса CsvParser, передать параметром путь к файлу .csv
2. Вызвать метод CsvParser.parse
3. Создать экземпляр класса Criterion(FirstCriterion, SecondCriterion, ThirdCriterion, FourthCriterion)
4. Вызвать метод CsvParser.apply, передать параметром экземпляр класса Criterion
5. Метод вернет количество записей, удовлетворяющих критерию

```
parser = CsvParser(path)
criterion = FirstCriterion()

parser.parse()
parser.apply(criterion) 
```

Для запуска пробного алгоритма, использующего класс CsvParser, выполнить ```python parser/__main__.py```
