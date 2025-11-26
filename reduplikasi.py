def reduplikasi(kalimat):
    kata = kalimat.split()
    i = 0
    fixed_list = []
    while i < (len(kata)-1):
        if kata[i] == kata[i+1]:
            fixed = kata[i] + '-' + kata[i+1]
            fixed_list.append(fixed)
            i+=+2
        else :
            fixed_list.append(kata[i])
            i+=1

    fixed_kalimat = " ".join(fixed_list)
    return fixed_kalimat