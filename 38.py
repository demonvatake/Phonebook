# Задача 38: Дополнить телефонный справочник возможностью добавления данных.


import csv


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по имени или фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Редактировать данные абонента в справочнике\n"
          "6. Удалить абонента из справочника\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input("Ваш выбор: "))
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')
    while (choice != 8):
        if choice == 1:
            for i in phone_book:
                print(i)
            choice = show_menu()

        elif choice == 2:
            # find_name(surname,name)
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            for i in phone_book:
                if i['Имя'] == name:
                    print(i)
                else:
                    if i['Фамилия'] == surname:
                        print(i)
            choice = show_menu()
        elif choice == 3:
            phone = input("Введите номер телефона: ")
            for i in phone_book:
                if i['Телефон'] == phone:
                    print(i)
            choice = show_menu()
        elif choice == 4:
            # create_new_user()
            new_data()
            choice = show_menu()


        elif choice == 7:
            save_txt(phone_book,None)





def read_csv(filename):
    data = list()
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data





def save_txt(file, phone_book1):
    with open(file, 'w', encoding='utf-8') as fin:
        for i in range(len(phone_book1)):
            string = ""
            for w in phone_book1[i].values():
                string += w + ','
            fin.write(f'{string[:-1]}\n')



def create_new_user(surname='', name='', phone=''):
            phone_book = read_csv('phonebook.csv')
            surname=input("Введите фамилию: ")
            name=input("Введите имя: ")
            phone=input("Введите телефон: ")
            # phone_book['Фамилия']=surname
            # phone_book['Имя']=name
            # phone_book['Телефон']=phone
            new_row = [surname.title(), name.title(), phone]
            phone_book.append(new_row)
            print("Контакт успешно добавлен!")

def new_data():
    """добавляет строку в справочник"""
    surname=input("Введите фамилию: ")
    name=input("Введите имя: ")
    phone=input("Введите телефон: ")
    with open('phonebook.csv', 'a', encoding='utf-8') as file:
        # file.write(input('Введите новую строку:'+ '\n') )
        file.write(f"{surname},{name},{phone}\n")
    print("Контакт успешно добавлен!")

 


# def create_new_user(surname='', name='', phone='', email=''):
#     surname=input("Введите фамилию: ")
#     name=input("Введите имя: ")
#     phone=input("Введите телефон: ")
#     email=input("Введите описание(имейл): ")
#     if(surname == ''):
#         print("ОШИБКА: НЕ УКАЗАНА ФАМИЛИЯ!!!!!1111")
#         return
#     if(name == ''):
#         print("ОШИБКА: НЕ УКАЗАНО ИМЯ!!!!!1111")
#         return
#     if(phone == ''):
#         print("ОШИБКА: НЕ УКАЗАН ТЕЛЕФОННЫЙ НОМЕР!!!!!1111")
#         return
#     if(email == ''):
#         print("ОШИБКА: НЕ УКАЗАН АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ!!!!!1111")
#         return
#     for row in phone_book:
#         if(row[1] == surname.title() and row[2] == name.title() and row[3] == phone and row[4] == email.lower()):
#             print("ТАКОЙ АБОНЕНТ УЖЕ СУЩЕСТВУЕТ")
#             return
#     new_row = [surname.title(), name.title(), phone, email.lower()]
#     phone_book.append(new_row)
#     with open(filename, 'a', newline='') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',',
#                             quotechar='\'', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(new_row)   

work_with_phonebook()
# show_menu()
