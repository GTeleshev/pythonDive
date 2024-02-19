# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter


def remove_characters(text):
    spe_char_to_remove = [':', ';', '!', '?', ',', '[', ']', '(', ')', '\n', '"', '.', '']
    for character in spe_char_to_remove:
        text = text.replace(character, '')
    return text


def top_frequent_words(text):
    text = remove_characters(text)
    print(text)
    words = text.lower().split(' ')
    print(words)
    word_count = {}
    for word in words:
        if word in word_count and word != '':
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_dict = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


# Пример использования
text = """Python is a high-level, general-purpose programming language.
        Its design philosophy emphasizes code readability with the use of significant indentation.[31])
        Python is dynamically typed and garbage-collected. It supports multiple programming paradigms,
        including structured (particularly procedural), object-oriented and functional programming.
        It is often described as a "batteries included" language due to its comprehensive standard library.[32][33]
        Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language
        and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000. Python 3.0, released in 2008,
        was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020,
        was the last release of Python 2.[35]. Python consistently ranks as one of the most popular programming
        languages, and has gained widespread use in the machine learning community.
        Python was conceived in the late 1980s[40] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) 
        in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[41] 
        capable of exception handling and interfacing with the Amoeba operating system.[10] 
        Its implementation began in December 1989.[42] Van Rossum shouldered sole responsibility for the project, 
        as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities
        as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect 
        his long-term commitment as the project's chief decision-maker.[43] In January 2019, 
        active Python core developers elected a five-member Steering Council to lead the project.[44][45]
        Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, 
        cycle-detecting garbage collection, reference counting, and Unicode support.[46] Python 3.0, released 
        on 3 December 2008, with many of its major features backported to Python 2.6.x[47] and 2.7.x. Releases
         of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[48]
        """

top_words = top_frequent_words(text)
print(top_words)
