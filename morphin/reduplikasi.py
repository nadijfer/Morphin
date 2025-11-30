'''
Kode ini berfungsi untuk memperbaiki adanya kesalahan reduplikasi kata, seperti "buku buku" (kurang tanda hubung).

ALGORITMA:
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

# in[0]:
# print(reduplikasi('bunga bunga dan buku buku')) 
# out[0]: bunga-bunga dan buku-buku
