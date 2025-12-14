# 1. perbaiki imbuhan: awalan
'''
1.1. metode periksa aturan
    1. Identifikasi letak awalan me
    2. Periksa peleburan me-:
        1. meng-    jika a, i, u, e, o, g, h, dan kh, k
        2. men-     jika c, d, j, t
        3. mem-     jika b, f, v, p
        4. me-      jika r, l, w, y, m, n, ng, dan ny
    3. periksa kata dasar setelah awalan yang salah
    4. perbaiki sesuai poin no. 2
1.2. metode window-based
    1. stem kata
'''

def perbaiki_awalan(kata):
    fixed = kata
    if kata.startswith('meng'):
        if kata[4] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
            fixed = kata
        elif kata[4] in 'k':
            fixed = 'meng'+kata[5:]
        else:
            # print('DARI MENG-')
            if kata[4] in ('c', 'd', 'j'):
                fixed = 'men' + kata[4:]
            elif kata[4] in ('b', 'f', 'v'):
                fixed = 'mem' + kata[4:]
            elif kata[4] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
                fixed = 'me' + kata[4:]
    elif kata.startswith('men'):
        if kata[3] in ('c', 'd', 'j'):
            fixed = kata
        elif kata[3] in 't':
            fixed = 'men'+kata[4:]
        elif kata[3] in 's':
            fixed = 'meny'+kata[4:]
        else:
            # print('DARI MEN-')
            if kata[3] in ('b', 'f', 'v'):
                fixed = 'mem' + kata[3:]
            elif kata[3] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
                fixed = 'me' + kata[3:]
            elif kata[3] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
                fixed = 'meng' + kata[3:]
    elif kata.startswith('mem'):
        if kata[3] in ('b', 'f', 'v'):
            fixed = kata
        elif kata[3] in 'pr':
            fixed = 'mem'+kata[4:]
        elif kata[3] in 'p':
            fixed = 'mem'+kata[4:]
        else:
            # print('DARI MEM-')
            if kata[3] in ('c', 'd', 'j'):
                fixed = 'men' + kata[3:]
            elif kata[3] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
                fixed = 'me' + kata[3:]
            elif kata[3] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
                fixed = 'meng' + kata[3:]
    elif kata.startswith('me'):
        if kata[2] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
            fixed = kata
        else:
            # print('DARI ME-')
            if kata[2] in ('c', 'd', 'j'):
                fixed = 'men' + kata[2:]
            elif kata[2] in ('b', 'f', 'v'):
                fixed = 'me' + kata[2:]
            elif kata[2] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
                fixed = 'meng' + kata[2:]
    return fixed

def perbaiki_nya(kata):
    fixed_list = kata.split()
    for i in range(len(fixed_list)):
        if fixed_list[i] == 'nya':
            fixed = fixed_list[i-1].join
            fixed = "".join(fixed_list)
    return fixed

# perbaiki reduplikasi
'''
1. Tokenisasi kalimat dengan fungsi .split() -> menjadi list $kata: String
2. Perulangan (looping) selama indeks $i kurang dari panjang $kata
    IF $kata pada indeks ke-$i (sekarang) sama dengan setelahnya:
        sisipkan "-" di antaranya dan masukkan ke dalam list kalimat benar
    ELSE:
        masukkan kata tersebut ke list kalimat yang benar
'''

def reduplikasi(kalimat):
    kata = kalimat.split()
    i = 0
    fixed_list = []
    while i < (len(kata)-1):
        if kata[i] == kata[i+1]:
            fixed = kata[i] + '-' + kata[i+1]
            fixed_list.append(fixed)
            i+=2
        else :
            fixed_list.append(kata[i])
            i+=1

    fixed_kalimat = " ".join(fixed_list)
    return fixed_kalimat


def perbaiki_kalimat(kalimat):
    print(f'kalimat salah: {kalimat}')
    pecah = kalimat.split()
    for i in range(len(pecah)):
        if pecah[i].startswith('me'):
            pecah[i] = perbaiki_awalan(pecah[i])
            print(f'perbaikan (list): {pecah}, kata: {pecah[i]}')
    fixed = " ".join(pecah)
    return fixed