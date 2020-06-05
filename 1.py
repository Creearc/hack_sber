import csv
import io

with io.open('bad.csv', encoding='utf-8') as f:
  s = csv.reader(f, delimiter=';', quotechar=';',
                        quoting=csv.QUOTE_MINIMAL)
  print(s)
  for row in s:
    print(row)
