print(ord('а'))
print(ord('я'))
print(ord('о'))



def norm(c):
  sr = ord('а') + (ord('я') - ord('а')) / 2
  return (ord(c) - sr - ord('а')) / sr


print(norm('а'))
print(norm('я'))
print(norm('о'))
print(norm('д'))
