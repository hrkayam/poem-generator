import codecs
from aksharamukha import transliterate
import io

# import polyglot
# from polyglot.text import Text

def romanize_file(fname):
    with codecs.open(fname + ".txt", encoding='utf-8') as f:
        parsed = f.readlines()

    parsed = [x.strip() for x in parsed]

    trans_list = []
    print(parsed)
    for word in parsed:
        text = word
        translated_txt = transliterate.process('Telugu', 'ISO', word)
        print(word)
        print(translated_txt)
        trans_list.append(translated_txt)

    with io.open(fname + "_transliterated.txt", "w", encoding="utf-8") as f:
        for padam in trans_list:
            f.write(padam + '\n')

    return trans_list
