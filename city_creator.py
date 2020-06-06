import io
f = io.open("selo.txt", encoding='utf-8')
ss =''

names = set()

mx = 0
ss = ''

for s in f:
  s = s.partition(' ')
  s = s[2].partition(' ')[2]
  s = s.split()
  if len(s) == 1:
    s = s[0]
    if s.isalpha():
      if mx < len(s):
        mx = len(s)
        ss = s
      names.add(s)

print(ss)
print(mx)
exit

names = list(names)
names.sort()

f = open("selo_list_short.txt", 'w')
for s in names:
  f.write('{}\n'.format(s))
f.close()

