def int_func():
    letter = input("Введите слова из маленьких латинских букв:").split()
    letter_str = letter.__str__()
    letter_str=letter_str.title()
    return letter_str
print(int_func())
