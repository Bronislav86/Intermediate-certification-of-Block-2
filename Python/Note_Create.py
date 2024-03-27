import datetime

def new_id():
    with open ('NoteBook.csv', 'r', encoding='utf-8') as file:
        data = file.read()
    if len(data) == 0:
        return 1
    id_list = data.rstrip().split("\n\n")
    print(id_list)
    return len(id_list) + 1


def input_title():
    return input("Введите заголовок заметки: ")


def input_note():
    return input("Введите текст заметки: ")


def current_date():
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return date


def create_note():
    data = f'{new_id()}\n{input_title()}\n{input_note()}\n{current_date()}\n'
    return data