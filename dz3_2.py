a = {'one': 'один', 'two': 'два'}


def num_translate_adv(eng_word):
    eng_word = input('Введите слово ')
    if eng_word.islower():
        eng_word = eng_word.lower()
        for key in a:
            if key == eng_word:
                return a[eng_word]

    else:
        eng_word = eng_word.lower()
        for key in a:
            if key == eng_word:
                return a[eng_word].capitalize()


print(num_translate_adv('one'))
