import re


# Функция для преобразования числа в пропись
def convert_number_to_words(number):
    words_dict = {
        '0': 'нуль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять',
        '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '10': 'десять',
        '11': 'одиннадцать', '12': 'двенадцать', '13': 'тринадцать', '14': 'четырнадцать',
        '15': 'пятнадцать', '16': 'шестнадцать', '17': 'семнадцать', '18': 'восемнадцать',
        '19': 'девятнадцать', '20': 'двадцать', '30': 'тридцать', '40': 'сорок',
        '50': 'пятьдесят', '60': 'шестдесят', '70': 'семьдесят', '80': 'восемьдесят',
        '90': 'девяносто'
    }
    if str(number) in words_dict:
        return words_dict[str(number)]
    elif 20 <= number < 100:
        tens = (number // 10) * 10
        ones = number % 10
        return words_dict[str(tens)] + (' ' + words_dict[str(ones)] if ones > 0 else '')
    return str(number)  # Для чисел больше 99 выводим просто число


# Функция для поиска чисел в файле и обработки их
def process_file(file_name, k):
    # Считываем весь текст из файла
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    # Находим все числа в тексте
    numbers = re.findall(r'\d+', content)
    numbers = list(map(int, numbers))  # Преобразуем найденные строки в числа

    # Разбиваем числа на десятки
    decade_groups = {}
    for num in numbers:
        decade = (num // 10) * 10  # Определяем десяток
        if decade not in decade_groups:
            decade_groups[decade] = []
        decade_groups[decade].append(num)

    # Проверка десятков на повторяющиеся числа
    lexemes = []
    for decade, group in decade_groups.items():
        # Подсчитываем сколько раз встречаются числа в десятке
        num_counts = {}
        for num in group:
            num_counts[num] = num_counts.get(num, 0) + 1

        # Если в десятке есть число, которое повторяется больше чем k раз, выводим десяток
        if any(count > k for count in num_counts.values()):
            result = []
            for num in group:
                if num == group[-1]:  # последнее число десятка
                    result.append(convert_number_to_words(num))
                else:
                    result.append(str(num))
            lexemes.append(' '.join(result))

    return lexemes


# Пример использования
file_name = 'input.txt'  # Имя файла с числами
k = int(input('Введите K: '))
lexemes = process_file(file_name, k - 1)  # Обрабатываем числа, повторяющиеся больше чем K раз

# Выводим результат
for lexeme in lexemes:
    print(lexeme)
