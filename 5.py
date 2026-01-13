import random


def get_jokes(jokes):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    for i in range(jokes):
        joke.append(f"{nouns[random.randint(0, 4)]} {adverbs[random.randint(0, 4)]} {adjectives[random.randint(0, 4)]}")
    return joke


count = int(input("Сколько шуток вы хотите?\n"))
print(get_jokes(count))


