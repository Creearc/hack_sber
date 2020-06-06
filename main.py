import csv
import io
import pickle
import roman
import time

check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mass = [{'область', 'обл.', 'обл'},
        {'г', 'г.', 'город', 'ст.', 'деревня', 'д.'},
        {'пос'},
        {'район', 'р-он', 'р-н.', 'р-н', 'м.', 'округ'},
        {'метро'},
        {'улица', 'пр-кт', 'пр-кт.', 'пер', 'пер.', 'ул.', 'ш.', 'ул', 'ш ', 'шоссе', 'проезд'},
        {'дом', 'д', 'д.'},
        {'строение', 'стр.', 'с.', 'с'},
        {'корп.'},
        {'этаж' 'эт.'},
        {'помещение', 'офис', 'пом.', 'к.', 'оф.', 'комн', 'ком.', 'ком', 'кв.'},
        {'офис'}]
tochka = []
for i in range(len(mass)):
    tochka.append(set())

for i in range(len(mass)):
    for j in mass[i]:
        if j.endswith('.'):
            tochka[i].add(j)
viktor = {'i', 'v', 'x', 'l', 'c', 'd', 'm'}


def rome():
    words[-1] = roman.fromRoman(s.upper())
    out[-1] = -1
    return out


def int_or_str(stroka):
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
        else:
            if (out[i] > 50) and not (int_or_str(words[i - 1]) or int_or_str(words[i + 1])):
                out[i] = 0
    return out, words


def make_result(arr):
    out, words = arr[0], arr[1]
    s = ''
    for i in range(len(out)):
        if out[i] != 0:
            s = '{} {}'.format(s, words[i])
    return s


t = time.time()
answer = set()
spisok = []
numbers = '1234567890'
with io.open('bad.csv', encoding='utf-8') as f:
    s = csv.reader(f, delimiter=';')
    with io.open('result_Kruassan.csv', "w", encoding='utf-8') as f2:
        for row in s:
            if row[0] == 'id':
                continue
            stroka = row[1]
            stroka = stroka.replace('!', '')
            stroka = stroka.replace('/', '\\')
            stroka = stroka.replace('%', '')
            f2.write("{};{};{}\n".format(row[0], row[1], make_result(vector(stroka))))
            #print([row[0], row[1], make_result(vector(stroka))])

print(time.time() - t)
print('Done!')

