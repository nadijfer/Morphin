from morphin import perbaiki

awalan = perbaiki.perbaiki_awalan
perbaiki_kalimat = perbaiki.kalimat_awalan

kalimat = 'aku disuruh ibu untuk pergi mensapu halaman'

hasil = perbaiki_kalimat(kalimat)
print(hasil)