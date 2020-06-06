import pickle

with open("arr.dat", 'rb') as f:
    arr = pickle.load(f)


def a(stroka):
    pass


def b(stroka):
    stroka = stroka.spliy(',')
    for elem in stroka:
        pass


def c(stroka, ind):
    if ind == 0:
        x = find_cstrana(stroka)
        if x != None:
            return x, ind
    elif ind == 1:
        x = find_region(stroka)
        if x != None:
            return x, ind
    elif ind == 2:
        x = find_gorod(stroka)
        if x != None:
            return x, ind
    elif ind == 3:
        x = find_mesto(stroka)
        if x != None:
            return x, ind
    elif ind == 4:
        x = find_type_of_raion(stroka)
        if x != None:
            return x, ind
    elif ind == 5:
        x = find_raion(stroka)
        if x != None:
            return x, ind
    elif ind == 6:
        x = find_type_of_(stroka)
        if x != None:
            return x, ind
    elif ind == 7:
        x = find_region(stroka)
        if x != None:
            return x, ind
    elif ind == 8:
        x = find_region(stroka)
        if x != None:
            return x, ind
    elif ind == 9:
        x = find_region(stroka)
        if x != None:
            return x, ind
    elif ind == 10:
        x = find_region(stroka)
        if x != None:
            return x, ind
    elif ind == 11:
        x = find_region(stroka)
        if x != None:
            return x, ind
    elif ind == 12:
        x = find_region(stroka)
        if x != None:
            return x, ind
    elif ind == 13:
        x = find_region(stroka)
        if x != None:
            return x, ind


def int_or_str(stroka):
    if stroka.isdigit() and not stroka.isalpha():
        return True
    else:
        return False


def find_region(stroka):
    shablons = ['область', 'обл']
    for shablon in shablons:
        if shablon in stroka:
            text = stroka.partition(shablon)
            t1, t2 = '', ''
            t1 = t1.join(text[0].split(',')).split()
            t2 = t2.join(text[-1].split(',')).split()
            if t1[-1].endswith('ый'):
                return t1
            elif t2[0].endswith('ый'):
                return t2
            break


def find_by_word(stroka, ends, shablons):
    for shablon in shablons:
        if shablon in stroka:
            text = stroka.partition(shablon)
            t1, t2 = '', ''
            t1 = t1.join(text[0].split(',')).split()
            t2 = t2.join(text[-1].split(',')).split()
            for end in ends:
                if t1[-1].endswith(end):
                    return t1
                elif t2[0].endswith(end):
                    return t2
                break
    return None


def find_by_number(stroka, shablons):
    for shablon in shablons:
        if shablon in stroka:
            text = stroka.partition(shablon)
            t1, t2 = '', ''
            t1 = t1.join(text[0].split(',')).split()
            t2 = t2.join(text[-1].split(',')).split()
            if int_or_str(t1[-1]):
                return t1
            elif int_or_str(t2[0]):
                return t2
            break
    return None


def find_dom(stroka):
    shablons = ['д.', 'дом ', 'д ', 'шоссе,']
    ends = ['ого', 'ова', 'ина', 'ой', 'ей', 'ы', 'ая', 'а']
    return find_by_number(stroka, shablons)


def find_ulitsa(stroka):
    shablons = ['улица', 'ул.', 'ул ', ]
    ends = ['ого', 'ова', 'ина', 'ой', 'ей', 'ы', 'ая', 'а']
    return find_by_word(stroka, ends, shablons)


def find_shosse(stroka):
    shablons = ['ш.', 'шоссе ', 'шоссе', 'шоссе,']
    ends = ['ое', 'ов']
    return find_by_word(stroka, ends, shablons)


def find_krai(stroka):
    shablons = ['край', 'кр ', 'кр.']
    ends = ['ий']
    return find_by_word(stroka, ends, shablons)


def find_oblast(stroka):
    shablons = ['область', 'обл.', 'обл ']
    ends = ['ая']
    return find_by_word(stroka, ends, shablons)


def find_type(stroka):
    stroka = stroka.split(' ')
    print(stroka)
    for elem in stroka:
        elem = elem.replace(',', '')
        for i in range(len(arr[0])):
            if arr[0][i] in elem:
                print(arr[1][i])
                print(arr[1].index(arr[1][i]) + 1)
            elif arr[0][i][:-1] in elem:
                print(arr[1][i])
                print(arr[1].index(arr[1][i]) + 1)
            else:
                a(stroka)


print(find_obl('Московская область, г.Королев, ул. Огарева, дом 15'))
'''
s = 'г.Пермь, ул.Луначарского 103'
#
s = 'г. Пермь ул.Луначарского 103'
#
s = 'Пермь г, ул.Луначарского 103'
#
s = 'Пермь Луначарского 103'
'''
