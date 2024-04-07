from model import write_data, print_data, edit_data, delete_data, print_data_line, print_date_selection

def interface():
    print("Main: \n ",
          "1 - Data recording \n ",
          "2 - Data output \n ",
          "3 - Data edit \n ",
          "4 - Data delete \n ",
          "5 - Output of a specific note \n ",
          "6 - Select note by date")
    command = int(input('Select command: '))  # принимаем данные из консоли сразу в виде числа

    while command not in range(1,7):  # если введено не число от 1 до 6 включительно, просим пользователя повторить ввод
        print("Invalid command")
        command = int(input('Enter number 1-6: '))

    if command == 1:
        write_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        delete_data()
    elif command == 5:
        print_data_line()
    elif command == 6:
        print_date_selection()
