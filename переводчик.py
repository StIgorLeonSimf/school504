from translate import Translator

trans_ru_en = Translator(from_lang='ru', to_lang='en')
word = input('Текст: ')
answer = trans_ru_en.translate(word.capitalize())
print(answer)
