from os.path import exists
import requests
import json

if not exists('livro.txt'):
    pathLivro = 'https://www.gutenberg.org/cache/epub/55682/pg55682.txt'
    r = requests.get(pathLivro, allow_redirects=True)
    open('livro.txt', 'wb').write(r.content)

data = open('quincasborba.txt', "r", encoding = "utf-8")

texto = data.read()

capitulos = ['PRIMEIRO', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L', 'LI', 'LII', 'LIII', 'LIV', 'LV', 'LVI', 'LVII', 'LVIII', 'LIX', 'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII', 'LXVIII', 'LXIX', 'LXX', 'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII', 'LXXVIII', 'LXXIX', 'LXXX', 'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI', 'LXXXVII', 'LXXXVIII', 'LXXXIX', 'XC', 'XCI', 'XCII', 'XCIII', 'XCIV', 'XCV', 'XCVI', 'XCVII', 'XCVIII', 'XCIX', 'C', 'CI', 'CII', 'CIII', 'CIV', 'CV', 'CVI', 'CVII', 'CVIII', 'CIX', 'CX', 'CXI', 'CXII', 'CXIII', 'CXIV', 'CXV', 'CXVI', 'CXVII', 'CXVIII', 'CXIX', 'CXX', 'CXXI', 'CXXII', 'CXXIII', 'CXXIV', 'CXXV', 'CXXVI', 'CXXVII', 'CXXVIII', 'CXXIX', 'CXXX', 'CXXXI', 'CXXXII', 'CXXXIII', 'CXXXIV', 'CXXXV', 'CXXXVI', 'CXXXVII', 'CXXXVIII', 'CXXXIX', 'CXL', 'CXLI', 'CXLII', 'CXLIII', 'CXLIV', 'CXLV', 'CXLVI', 'CXLVII', 'CXLVIII', 'CXLIX', 'CL', 'CLI', 'CLII', 'CLIII', 'CLIV', 'CLV', 'CLVI', 'CLVII', 'CLVIII', 'CLIX', 'CLX', 'CLXI', 'CLXII', 'CLXIII', 'CLXIV', 'CLXV', 'CLXVI', 'CLXVII', 'CLXVIII', 'CLXIX', 'CLXX', 'CLXXI', 'CLXXII', 'CLXXIII', 'CLXXIV', 'CLXXV', 'CLXXVI', 'CLXXVII', 'CLXXVIII', 'CLXXIX', 'CLXXX', 'CLXXXI', 'CLXXXII', 'CLXXXIII', 'CLXXXIV', 'CLXXXV', 'CLXXXVI', 'CLXXXVII', 'CLXXXVIII', 'CLXXXIX', 'CXC', 'CXCI', 'CXCII', 'CXCIII', 'CXCIV', 'CXCV', 'CXCVI', 'CXCVII', 'CXCVIII', 'CXCIX', 'CC', 'CCI']

livro = {}
for capitulo in capitulos:
    textoNaoFormatado = texto.split('CAPÍTULO')[capitulos.index(capitulo) + 1].strip()
    textoParagrafado = textoNaoFormatado.split(capitulo)[-1].strip()
    livro['CAPÍTULO ' + capitulo] = ' '.join(textoParagrafado.split('\n'))
    
from nltk.tokenize import word_tokenize

for key in livro:
    words = word_tokenize(livro[key])
    new_words = [value for value in words if value not in ('--', '_', '-', '–', '``', '\'\'')]
    import string
    formattedText = ''
    flag = True
    for index, word in enumerate(new_words):
        if flag:
            if index != 0:
                if word == '(':
                    formattedText += ' ' + word + new_words[index + 1]
                    flag = False
                elif word in string.punctuation or word == '...':
                    formattedText += word
                else:
                    formattedText += ' ' + word
            else:
                formattedText += word
        else:
            flag = not flag
    if key == 'CAPITULO CCI':
        livro[key] = formattedText.split('FIM')[0].strip().replace('_', '')
    else:
        livro[key] = formattedText.replace('_', '')

copy_livro = livro.copy()
for key in copy_livro:
    texto = copy_livro[key]
    words = word_tokenize(texto)
    noPunct = [value for value in words if value not in string.punctuation]
    size = len(noPunct)
    if size > 150 or size < 51:
        del(livro[key])

json_data = {'Quincas Borbas': livro}

with open('QuincasBorbasShortEasy.json', 'w', encoding='utf8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False)