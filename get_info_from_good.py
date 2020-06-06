import csv
import io
import pickle
"""
de = ["г.", "д.", "гор.", "оф."]

answer = set()
spisok = []
with io.open('good.csv', encoding='utf-8') as f:
  s = csv.reader(f, delimiter=';')
  for row in s:
    for i in row[1:]:
      for j in i.split():
        if j.isalpha():
          j = j.lower()
          for d in de:
            if not j.startswith(d):
              answer.add(j)
              


print(len(answer))
answer = list(answer)
answer.sort()
with open('vitya.dat', "wb") as f:
    pickle.dump(answer, f)




"""
with open('vitya.dat', 'rb') as f:
    answer = pickle.load(f)

v = []
v2 = []
ends_1 = ["ово", "ево", "ёво", "ино", "ыно"]
ends_2 = ["ий", "ая", "ый", "ора", "ала", "ого", "ое", "ева"]
ends_3 = ["ск", "дар", "град"]
ends = ends_1 + ends_2
for elem in answer:
  b = True
  for e in ends:
    if elem.endswith(e):
      v.append(elem)
      b = False
      continue
  if b:
    v2.append(elem)

print(v)
print(v2)

print(len(v2), len(v))

s = 'vitya'
i = 3
print(("{}{}{}").format(s[:i], 'Ё', s[i+1:]))
