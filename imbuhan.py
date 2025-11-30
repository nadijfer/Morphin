from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

kata = 'mengdapat'
stem = stemmer.stem(kata)
next_stem = stemmer.stem(stem)
kata_dasar = ''

for i in range(len(kata)):
    stem = stemmer.stem(kata)
    next_stem = stemmer.stem(stem)
    if kata == stem: # kata tidak bisa di-stem atau sudah di-stem
        kata = kata[i:]
        stem = stemmer.stem(kata)
        next_stem = stemmer.stem(kata)
        if next_stem == stem:
            kata_dasar = next_stem
            continue
    else:
        print("tidak sama")

print(kata_dasar)
# fase memperbaiki imbuhan
# if kata_dasar[0] in 'r|l|w|y|m|n|ng||ny.': # kondisi pertama
#     fixed = 'me' + kata_dasar
# elif kata_dasar[0] in 'b|f|v':
#   fixed = 'men' + kata_dasar
# elif kata_dasar[0] in 'c|d|j':
#   fixed = 'men' + kata_dasar
# elif kata_dasar[0] in 'a|i|u|e|o|g|h|kh':
#   fixed = 'meng' + kata_dasar

# print(fixed)
# if hasKan:
#   fixed += 'kan'
# elif hasLah:
#   fixed += 'lah'

# print(f'kata yang telah diperbaiki: {fixed}')
            
            
# print(kata, stem, next_stem)
# kata = kata[1:]
# stem = stemmer.stem(kata)
# print(kata, stem, next_stem)
# next_stem = stemmer.stem(stem)

# kata = kata[1:]
# stem = stemmer.stem(kata)
# print(kata, stem, next_stem)
# next_stem = stemmer.stem(stem)

# kata = kata[1:]
# stem = stemmer.stem(kata)
# print(kata, stem, next_stem)
# next_stem = stemmer.stem(stem)

# kata = kata[1:]
# stem = stemmer.stem(kata)
# print(kata, stem, next_stem)
# next_stem = stemmer.stem(stem)

# kata = kata[1:]
# stem = stemmer.stem(kata)
# print(kata, stem, next_stem)
# next_stem = stemmer.stem(stem)

# print(next_stem == stem)