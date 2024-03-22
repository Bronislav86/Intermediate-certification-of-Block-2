from datetime import datetime
import json

int id_num = 0


def id():
    id_num += 1
    return  id_num


def input_title():
    return input("Введите заголовок заметки: ")


def input_note():
    return input("Введите текст заметки: ")


def current_date():
    return datetime.timestamp()


def create_note():
    data = {
        "count": id(),
        "title": input_title(),
        "note": input_note(),
        "date": current_date(),
    }

    json_data = json.dumps(data)
    
    return json_data

def add_note (note):
    with open('NoteBook.json', 'r', encoding='URF-8') as file:
        file.write(note)