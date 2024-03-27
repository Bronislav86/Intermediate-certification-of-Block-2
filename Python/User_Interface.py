from Logger import *

def user_menu():
    command = "-1"
    while command != "6":
        print(
            "Меню:\n"
            "1. Показать все записи\n"
            "2. Добавить заметку\n"
            "3. Найти заметку\n"
            "4. Редактировать заметку\n"
            "5. Удалить заметку\n"
            "6. Выход\n"
        )
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Ошибка ввода")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                show_notes()
            case "2":
                add_note()
            case "3":
                find_note()
            case "4":
                edit_note()
            case "5":
                delete_note()
            case "6":
                print("Всего хорошего!")