import random

def get_word():
    word_list = ["олень", "слон", "жираф", "кенгуру", "тигр", "леопард", "зебра"]
    return random.choice(word_list)

def create_table(word):
    return ["\u25A0" for _ in word]

def get_lives(word):
    return len(word)

def is_alive(lives):
    return lives > 0

def show_table(table):
    display = " ".join(table)
    print(display)

def get_player_input():
    return input("Угадайте букву или введите слово целиком: ").lower()

def is_word_correct(word, answer):
    return word == answer

def is_letter_correct(word, letter):
    return letter in word

def update_table(word, table, letter):
    for i, char in enumerate(word):
        if char == letter:
            table[i] = letter

def play_hangman():
    word = get_word()
    table = create_table(word)
    lives = get_lives(word)
    
    print("Добро пожаловать в игру 'Виселица на поле чудес'!")
    print("У вас есть", lives, "жизней.")
    
    while is_alive(lives):
        show_table(table)
        answer = get_player_input()
        
        if len(answer) == 1:
            if is_letter_correct(word, answer):
                print("Правильно! Буква", answer, "находится в слове.")
                update_table(word, table, answer)
                if "".join(table) == word:
                    print("Поздравляем! Вы угадали слово:", word)
                    break
            else:
                print("Неправильно! Буквы", answer, "нет в слове.")
                lives -= 1
        elif is_word_correct(word, answer):
            print("Поздравляем! Вы угадали слово:", word)
            break
        else:
            print("Неправильный ввод. Пожалуйста, введите одну букву или слово целиком.")
    
    if lives == 0:
        print("Игра окончена. Загаданное слово было:", word)
