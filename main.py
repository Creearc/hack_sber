import csv
import io
import pickle
import roman
import time
import threading

numbers = '1234567890'

mass = [{'область', 'обл.', 'обл'},
        {'г', 'г.', 'город', 'ст.', 'деревня', 'д.'},
        {'пос'},
        {'район', 'р-он', 'р-н.', 'р-н', 'м.', 'округ'},
        {'метро'},
        {'улица', 'пр-кт', 'пр-кт.', 'ул.', 'ш.', 'ул', 'ш ', 'шоссе', 'проезд'},
        {'переулок', 'пер', 'пер.'},
        {'дом', 'д', 'д.'},
        {'строение', 'стр.', 'с.', 'с'},
        {'корп.'},
        {'этаж' 'эт.'},
        {'помещение', 'пом.', 'кв.'},
        {'к.', 'комн', 'ком.', 'ком'},
        {'офис', 'оф.'}]

tochka = []
for i in range(len(mass)):
    tochka.append(set())

for i in range(len(mass)):
    for j in mass[i]:
        if j.endswith('.'):
            tochka[i].add(j)
viktor = {'i', 'v', 'x', 'l', 'c', 'd', 'm'}

vec = set()

def rome():
    words[-1] = roman.fromRoman(s.upper())
    out[-1] = -1
    return out


def int_or_str(stroka):
    stroka = str(stroka)
    if stroka.isdigit() and not stroka.isalpha():
        return True
    else:
        return False


def c_detector(stroka):
    out = stroka.partition('с')
    if out[1] == 'с':
        return out, True
    else:
        return stroka, False


def vector(stroka):
    check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stroka = stroka.split(',')
    out = []
    words = []
    for elem in stroka:
        elem = elem.split()
        for s in elem:
            out.append(int(0))
            words.append(s)
            s = s.lower()
            if int_or_str(s):
                out[-1] = -1
            else:
                if s[0] in viktor:
                    b = True
                    for i in s:
                        if i not in viktor:
                            b = False
                            break
                    if b:
                        try:
                            words[-1] = roman.fromRoman(s.upper())
                            out[-1] = -1
                        except:
                            pass

                for i in range(len(mass)):
                    if s in mass[i]:
                        if check[i] == 0:
                            out[-1] = (i + 1) * 10
                            check[i] = 1
                            break
                for i in range(len(tochka)):
                    for j in tochka[i]:
                        if s.startswith(j):
                            out[-1] = i + 1
                            break

    for i in range(len(out) - 1):
        if out[i] > 0:
            if i > 0:
                if out[i - 1] == 0:
                    out[i - 1] = -2
            if i < len(out):
                if out[i + 1] == 0:
                    out[i + 1] = -2
        if (out[i] > 80) and not (int_or_str(words[i - 1]) or int_or_str(words[i + 1])):
            out[i] = 0
    

    return out, words


def arr_to_s(arr):
    out = ''
    for i in arr:
        if i != 0:
            out = '{}.{}'.format(out, str(i))
    return out


def make_result(arr):
    out, words = arr[0], arr[1]
    s = ''
    for i in range(len(out)):
        if out[i] != 0:
            s = '{} {}'.format(s, words[i])
    return s

def mvec(stroka):
    stroka = stroka.split()
    out = ''
    for s in stroka:
        pass
        


def worker(ind, step, text):
    global answer, lock
    out = []

    for s in text:
        row = s.split(';')
        stroka = row[1]
        stroka = stroka.replace('!', '')
        stroka = stroka.replace('/', '\\')
        stroka = stroka.replace('%', '')
        #out.append([row[0], row[1], mvec(stroka)])
        out.append([row[0], row[1], make_result(vector(stroka))])
      
    with lock:
        answer[ind] = out
    return


lock = threading.Lock()


if __name__ == "__main__":
    tm = time.time()

    threads = []

    proc = 30
    answer = []
    text = []
    for i in range(proc):
        answer.append([])
        text.append([])

    f = io.open('bad.csv', encoding='utf-8')
    i = -1
    for s in f:
        if i == -1:
            i = 0
            continue
        text[i].append(s)
        i+=1
        if i > proc - 1:
            i = 0
    f.close()
    print(time.time() - tm)
    tm = time.time()

    for i in range(proc):
        t = threading.Thread(target=worker, args=(i, proc, text[i]))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(time.time() - tm)
    tm = time.time()
    
    with io.open('result_Kruassan.csv', "w", encoding='utf-8') as f2:
        while len(answer[0]) > 0:
            for i in range(len(answer)):
                if answer[i] == []:
                    break
                x = answer[i].pop(0)
                f2.write("{};{};{}\n".format(x[0], x[1][:-1], x[2]))

    print(time.time() - tm)
    print('Done!')

