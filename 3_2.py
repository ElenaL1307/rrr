phrase = input('Введите текст: ')
letters = {i: phrase.count(i) for i in phrase}
print(letters)