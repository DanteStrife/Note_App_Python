from data import id_data, title_data, text_data
from datetime import datetime
import json


def write_data():  # создаем новую заметку
    id = id_data()
    title = title_data()
    text = text_data()
    with open('notes.json', 'a', encoding='utf-8') as f:
        time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        f.write(f"{id}  |{title}         |{text}        |{time}\n")


def edit_data():  # Изменяем заметки
    n = int(input('Enter the id of the entry you want to change '))
    write_data()  # Вызываем функцию для записи новых данных в конец файла и дальнейшей записи в нужную строку

    with open('notes.json', 'r', encoding='utf-8') as f:
        notes = f.readlines()
        edit_el = notes.pop()
        notes_list = notes[:n - 1] + [edit_el] + notes[n:]
    with open('notes.json', 'w', encoding='utf-8') as f:
        f.writelines(notes_list)


def delete_data():  # Удаляем заметку файла
    n = int(input('Enter the entry id to delete: '))

    with open('notes.json', 'r', encoding='utf-8') as f:
        notes = f.readlines()
        notes_list = notes[:n - 1] + notes[n:]
    with open('notes.json', 'w', encoding='utf-8') as f:
        f.writelines(notes_list)


def print_data():  # выводим данные из файла с заметками в терминал
    print('Extracting data from a file with notes: \n')


with open('notes.json', 'r', encoding='utf-8') as f:
    notes = f.readlines()  # прочитали все наши строки
    print(*notes)  # выводим данные на печать, с распаковкой через *


def print_data_line():  # выводим данные из файла с заметками в терминал
    n = int(input('Enter note number to print: '))

    with open('notes.json', 'r', encoding='utf-8') as f:
        if n not in range(
                len(f.readlines())):  # если введено не число в рамках количества заметок, просим пользователя повторить ввод
            print("No note under number ", n)
            print_data_line()
        else:
            print("I'm writing a note under the number: ", n)
            f.seek(0)  # возвращаемся к началу файла
            notes = f.readlines()  # прочитали все наши строки
            print(notes[n - 1])


def print_date_selection():
    with open('notes.json', 'r', encoding='utf-8') as json_file:
        search_value = input("Enter the date the file was recorded/modified to search in the format DD.MM.YYYY: ")
        for row in json_file:
            if search_value in row:
                print(row)
            else:
                print("Record not found.")
                break
