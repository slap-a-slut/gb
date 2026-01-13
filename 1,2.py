NUMTRANS1 = {"zero": 'ноль', "one": 'один', "two": 'два', "three": 'три', "four": 'четыре',
      "five": 'пять', "six": 'шесть', "seven": 'семь', "eight": 'восемь', "nine": 'девять', "ten": 'десять'}
NUMTRANS2 = {"zero": 'ноль', "One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре',
       "Five": 'Пять', "Six": 'Шесть', "Seven": 'Семь', "Eight": 'Восемь', "Nine": 'Девять', "Ten": 'Десять'}


def num_translate_adv(a):

        if NUMTRANS1.get(a) is None:
            print(NUMTRANS2.get(a))
        else:
            print(NUMTRANS1.get(a))


num_translate_adv("Five")

