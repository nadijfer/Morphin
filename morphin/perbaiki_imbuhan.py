import re
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

def perbaiki_awalan_m(kata_list):
    fixed = []
    list_kata_dengan_koma = re.findall(r'\w+|[^\w\s]', kata_list)
    for kata in list_kata_dengan_koma:
        if kata.startswith('meng'):
          if kata[4] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
            fixed.append(kata)
          elif kata[4] in 'k':
            fixed.append('meng'+kata[5:]) 
          else:
            # print('DARI MENG-')
            if kata[4] in ('c', 'd', 'j'):
                fixed.append('men' + kata[4:])
            elif kata[4] in ('b', 'f', 'v'):
                fixed.append('me' + kata[4:]) 
            elif kata[4] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
                fixed.append('me' + kata[4:])
        elif kata.startswith('men'):
          if kata[3] in ('c', 'd', 'j'):
            fixed.append(kata)
          elif kata[3] in 't':
            fixed.append('men'+kata[4:])
          elif kata[3] in 's':
            fixed.append('meny'+kata[4:]) 
          else:
            # print('DARI MEN-')
            if kata[3] in ('b', 'f', 'v'):
                fixed.append('mem' + kata[3:]) 
            elif kata[3] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
                fixed.append('me' + kata[3:])
            elif kata[3] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
                fixed.append('meng' + kata[3:])
        elif kata.startswith('mem'):
          if kata[3] in ('b', 'f', 'v'):
            fixed.append(kata)
          elif kata[3] in 'pr':
            fixed.append('mem'+kata[4:]) 
          elif kata[3] in 'p':
            fixed.append('mem'+kata[4:])
          else:
            # print('DARI MEM-')
            if kata[3] in ('c', 'd', 'j'):
                fixed.append('men' + kata[3:]) 
            elif kata[3] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
                fixed.append('me' + kata[3:]) 
            elif kata[3] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
                fixed.append('meng' + kata[3:])
        elif kata.startswith('me'):
          if kata[2] in ('r', 'l', 'w', 'y', 'm', 'n', 'ng', 'ny'):
            fixed.append(kata)
          else:
            # print('DARI ME-')
            if kata[2] in ('c', 'd', 'j'):
                fixed.append('men' + kata[2:])
            elif kata[2] in ('b', 'f', 'v'):
                fixed.append('me' + kata[2:])
            elif kata[2] in ('a', 'i', 'u', 'e', 'o', 'g', 'h', 'kh'):
                fixed.append('meng' + kata[2:])
        else :
            fixed.append(kata)
    fixed = tokens_to_sentence(fixed)
    return fixed

def akhiran_nya(list_kata):
    """
    Memperbaiki kesalahan yang biasanya terjadi pada akhiran kata, seperti:
    'nya'
    'ku'
    'mu'
    yang biasanya terdapat spasi diantara kata dan akhiran
    """

    list_kata_dengan_koma = re.findall(r'\w+|[^\w\s]', list_kata)
    fixed = []
    klitik = {'nya', 'ku', 'mu'}

    for i in list_kata_dengan_koma:
        if i in klitik:
            fixed[-1] += i
        else:
            fixed.append(i)
    fixed = tokens_to_sentence(fixed)
    return fixed

def perbaiki_awalan_p(kata_list):
    """
    Memperbaiki kesalahan morfologi pada kata berimbuhan pe-an.
    Logika: Copot awalan yang salah -> Deteksi huruf awal -> Pasang awalan benar.
    Mencakup: perbaikan peluluhan (K,T,S,P) dan penyesuaian nasal (m/n/ng/ny).
    """


    fixed = []
    list_kata_dengan_koma = re.findall(r'\w+|[^\w\s]', kata_list)

    for kata in list_kata_dengan_koma:

          body = kata

          if kata.startswith('peng'):
              body = kata[4:]
          elif kata.startswith('peny'):
              body = kata[4:]
          elif kata.startswith('pem'):
              body = kata[3:]
          elif kata.startswith('pen'):
              body = kata[3:]
          elif kata.startswith('pe'):
              body = kata[2:]
          elif kata.startswith('per'):
              fixed.append(kata)
              continue
          else:
              fixed.append(kata)
              continue

          if len(body) < 3:
              fixed.append(kata)
              continue

          huruf_awal = body[0]

          if huruf_awal in ('b', 'f', 'v'):
              fixed.append('pem' + body)

          elif huruf_awal in ('c', 'd', 'j', 'z'):
              fixed.append('pen' + body)

          elif huruf_awal in ('g', 'h', 'a', 'i', 'u', 'e', 'o'):
              fixed.append('peng' + body)

          elif huruf_awal in ('l', 'r', 'w', 'y', 'm', 'n'):
              fixed.append('pe' + body)


          elif huruf_awal == 's':
              fixed.append('peny' + body[1:])

          elif huruf_awal == 'k':
              fixed.append('peng' + body[1:])

          elif huruf_awal == 'p':
              fixed.append('pem' + body[1:])

          elif huruf_awal == 't':
              fixed.append('pen' + body[1:])

    fixed = tokens_to_sentence(fixed)
    return fixed

def tokens_to_sentence(tokens):
    kalimat = ""
    tanda_baca = {",", ".", "!", "?", ":", ";"}

    for token in tokens:
        if token in tanda_baca:
            kalimat += token
        else:
            if kalimat and not kalimat.endswith(" "):
                kalimat += " "
            kalimat += token

    return kalimat

def perbaiki_semua(kalimat):
    kalimat = perbaiki_awalan_p(kalimat)
    kalimat = perbaiki_awalan_m(kalimat)
    kalimat = akhiran_nya(kalimat)
  
    return kalimat
