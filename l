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
    return str(number)  # Для чисел больше 100 выводим просто число


# Функция для обработки чисел из файла
def process_lexemes(file_name, k):
    lexemes = []
    decade_groups = {}  # Для группирования чисел по десяткам
    with open(file_name, 'r') as file:
        while True:
            block = file.read(1024)  # Чтение файла поблочно

            if not block:
                break

            for char in block:
                if char.isnumeric():
                    num = int(char)
                    decade = (num // 10) * 10  # Определяем десяток
                    if decade not in decade_groups:
                        decade_groups[decade] = []
                    decade_groups[decade].append(num)

    # Проверка десятков на повторяющиеся числа
    for decade, numbers in decade_groups.items():
        num_counts = {}
        for num in numbers:
            num_counts[num] = num_counts.get(num, 0) + 1

        # Если в десятке есть число, которое повторяется больше чем k раз, выводим десяток
        if any(count > k for count in num_counts.values()):
            result = []
            for num in numbers:
                if num == numbers[-1]:  # последнее число десятка
                    result.append(convert_number_to_words(num))
                else:
                    result.append(str(num))
            lexemes.append(' '.join(result))

    return lexemes


# Пример использования
file_name = 'input.txt'  # Имя файла с числами
k = int(input('Введите k: '))
lexemes = process_lexemes(file_name, k - 1)

# Выводим результат
for lexeme in lexemes:
    print(lexeme)
