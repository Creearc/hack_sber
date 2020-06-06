import time
import pickle
import numpy as np
import io


def f(s, T):
  if s <= 0: return 0
  elif s <= T: return s
  else: return T

def norm(c):
  sr = ord('а') + (ord('я') - ord('а')) / 2
  return (ord(c) - sr - ord('а')) / sr


def vec(s, l):
  out = np.zeros(l)
  for i in range(len(s)):
    out[i] = norm(s[i])
  return out
 

def calc1(inp, layer, T):
  for j in range(len(layer)):
    sm = 0
    for i in range(len(inp)):
      sm += inp[i]*layer[j][i]
    yield f(sm, T)


def calc2(inp, layer, T):
  for j in range(len(layer)):
    sm = 0
    for i in range(len(inp)):
      sm += inp[i]*layer[i][j]
    yield f(sm, T)


def train_net(vec_l, path="1.txt", debug=False):
  x = []
  f = io.open(path)
  for s in f:
    x.append(vec(s[:-1], vec_l))
  
  M = vec_l # размер вектора
  K = len(x) # количество шаблонов
  T = M / 2
  E = 1 / K # (0, 1/K]
  Emax = 0.1 # выбирается самостоятельно

  if debug: print('M={} K={} T={} E={}'.format(M, K, T, E))
  # Задаем веса первого слоя
  layer1 = np.multiply(x, 0.5)
  # Задаем веса второго слоя
  layer2 = np.diag(np.ones(K), k=0)
  layer2 [layer2  < 1] = -E
  return {'layer 1' : layer1, 'layer 2' : layer2,
          'M' : M, 'K' : K, 'T' : T, 'E' : E, 'Emax' : Emax,
          'VECTOR_SIZE' : vec_l}


def start_net(net, inp, debug=False):
  layer1_out = np.fromiter(calc1(inp, net['layer 1'], net['T']),dtype=float,count=-1)
  layer2_out_last = layer1_out.copy()
  for i in range(50): 
    layer2_out = np.fromiter(calc2(layer2_out_last, net['layer 2'], net['T']),dtype=float,count=-1)
    calc = np.linalg.norm(layer2_out - layer2_out_last)
    if debug: print('Iter {} {} {}'.format(i, layer2_out, calc))
    if  calc <= net['Emax']: break
    layer2_out_last = layer2_out.copy()
  return layer2_out.argmax()


def load_net(path):
  with open(path, 'rb') as f:
    net = pickle.load(f)
  return net


def save_net(net, path):
  with open(path, "wb") as f:
    pickle.dump(net, f)

vec_l = 26


if __name__== "__main__":

  net = train_net(vec_l, "selo_list_short.txt")
  save_net(net, 'net.dat')
  net = load_net('net.dat')
  vec_l= net['VECTOR_SIZE']

  # Запуск нейронной сети
  s = 'москва'
  t = time.time()
  inp = vec(vec_l, s)
  print(start_net(net, inp))
  print(time.time() - t)




