from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def perbaiki_kata_depan(kata):
    fixed = ''
    if stemmer.stem(kata) == kata:
        if kata.startswith('di') or kata.startswith('ke'):
            fixed = kata[:2] + ' ' + kata[2:]
        elif kata[:4].startswith('dari'):
            fixed = kata[:4] + ' ' + kata[4:]
        return fixed
    else: 
        return kata