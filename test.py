import io
import pickle

numbers = '1234567890'
chars = 'йцукенгшщзхъфывапролджэячсмитьбю'

def v(stroka):
  out = ' '
  t = False
  for c in stroka:
    if c in numbers:
      t = True
      if out[-1] != '1':
        out = '{}.{}'.format(out, 1)
    elif c in chars:
      if out[-1] != '2':
        out = '{}.{}'.format(out, 2)
    else:
      if out[-1] != '0':
        out = '{}.{}'.format(out, 0)
  return t, out[2:]

"""
b = set()

f = io.open('good.csv', encoding='utf-8')
for s in f:
  stroka = s.split(';')[1].split()
  for w in stroka:
    b.add(w.lower())

print('done')

b = list(b)
b.sort()

with open('1.dat', "wb") as f:
  pickle.dump(b, f)
"""

with open('1.dat', 'rb') as f:
    b = pickle.load(f)

c = set()

for s in b:
  t, o = v(s)
  if t:
    c.add(o)
"""
c = list(c)
c.sort()
print(c)
"""
