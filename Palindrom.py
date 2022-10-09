def cekpalindrom (teks) :
    lista = []
    belakang = ''
    depan = ''
    indikator = True
    for i in range (len(teks)) :
        if teks[i] != ',' and teks[i] != '.' and teks[i] != "'" and teks[i] != '"' and teks[i] != '!' and teks[i] != '?' and teks[i] != ' ' :
            lista.append(teks[i])
    while len(lista) > 1 and indikator  :
        depan += lista.pop(0)
        belakang += lista.pop()
        if belakang != depan :
            indikator = False
    if indikator :
        print(teks, "adalah kata palyndrom.")
    else :
        print(teks, "bukan kata palyndrom.")

a = input('masukkan teks : ')

print('hasil : ')
cekpalindrom (a)