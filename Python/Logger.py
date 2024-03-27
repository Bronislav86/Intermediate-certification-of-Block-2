from Note_Create import *

def add_note():
    note = create_note()
    
    with open("NoteBook.csv", "a", encoding="utf-8") as file:
        file.write(note)
        
    print("\nНовая заметка успешно добавлена!\n")


def show_notes():
    with open("NoteBook.csv", "r", encoding="utf-8") as file:
        data = file.read()
    print()
    print('Все заметки: \n')
    print(data)


def find_note():
    print()
    print('Для поиска нужной заметки, выберите нужную дату из списка: \n'
          '1. Поиск по id\n'
          '2. Поиск по заголовку\n'
          '3. По содержанию заметки\n'
          '4. Поиск по дате\n')
    print()
    
    command = input('Введите критерий поиска: \n')
    while command not in ('1', '2', '3', '4'):
        print('Некорректный ввод! Выберите вариант из списка.\n')
        command = input('Введите критерий поиска: \n')
        
    index = int(command) - 1
    search = input('Введите данне для поиска: \n')
    with open ('NoteBook.csv', 'r', encoding='utf-8') as file:
        data = file.read().rstrip().split('\n\n\n')
        for notes in data:
            notes_lst = notes.split('\n')
            if search in notes_lst[index]:
                print(notes_lst)
                return notes_lst

def edit_note():
    with open("notebook.csv", "r+", encoding="UTF-8") as file:
        data = file.read()
    notes_list = data.rstrip().split("\n\n\n")
    flag = True
    print()
    while flag:

        if len(data) == 0:
            print('Нет заметок для редактирования.')
            flag = False
                    
        size_list = len(notes_list)
        id_list = [str(i+1) for i in range(size_list)]
        id_for_edit = ''
        while id_for_edit not in id_list:
            id_for_edit = input('Введите номер заметки для редактирования: \n')
        edit_note = notes_list[int(id_for_edit) - 1]
        edit_notes_lst = edit_note.split("\n")
        new_note = ""
        while len(new_note) == 0:
            new_note = input('Введите новый текст:\n').strip()
        edit_notes_lst[2] = new_note
        notes_list[int(id_for_edit) - 1] =''
        for i in range (len(edit_notes_lst)):
            notes_list[int(id_for_edit) - 1] += f'{edit_notes_lst[i]}\n'
        notes_list[int(id_for_edit) - 1] = notes_list[int(id_for_edit) - 1].strip()
        data_to_write = ''
        for i in range(len(notes_list)):
            data_to_write += notes_list[i] + '\n\n\n'
            
        with open ('NoteBook.csv', 'w', encoding='utf-8') as file:
            file.write(data_to_write)
            print(f'Заметка {id_for_edit} успешно изменена.\n'
                  'Переход в главное меню.')
            flag = False

def delete_note():
    with open("notebook.csv", "r+", encoding="UTF-8") as file:
        data = file.read()
    notes_list = data.rstrip().split("\n\n\n")
    list_for_print =[]
    list_for_print.append(notes_list[1].split('\n'))
    flag = True
    print()
    while flag:

        if len(data) == 0:
            print('Нет заметок для удаления.')
            flag = False            
        note_list_size = len(notes_list)
        print(f"Заметки, доступные для удаления:\n\n{data}")
        id_list = [str(i+1) for i in range(note_list_size)]
        id_for_del = "0"
        while id_for_del not in id_list:
            id_for_del = input("Введите номер заметки для удаления: ")
        notes_list.pop(int(id_for_del)-1)
        for i in range(len(notes_list)):
            cur_note = notes_list[i].split("\n")
            cur_note[0] = str(i+1)
            notes_list[i] = ""
            for j in range(len(cur_note)):
                notes_list[i] += f"{cur_note[j]}\n"
        text = ""
        for i in range(len(notes_list)):
            text += notes_list[i]+"\n\n"
        with open("notebook.csv", "w", encoding="UTF-8") as file:
            file.write(text)
            flag = False
