# 1. perbaiki imbuhan: awalan
'''
1.1. metode periksa aturan
    1. Identifikasi letak awalan me
    2. Periksa peleburan me-:
        1. meng-    jika a, i, u, e, o, g, h, dan kh
        2. men-     jika c, d, j
        3. mem-     jika b, f, v
        4. me-      jika r, l, w, y, m, n, ng, dan ny
    3. periksa kata dasar setelah awalan yang salah
    4. perbaiki sesuai poin no. 2
'''

def imbuhan_awalan(kata):
    if kata.startswith('meng'):
        if kata[4] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
            fixed = kata
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