'''
Създайте програма, която:
• Дефинира структура на данни, моделираща данни за клиент на мобилен оператор.
• Данните съдържат информация за:
◦ клиентски номер
◦ телефонен номер
◦ име на клиента
◦ информация за проведени разговори (масив от 4 елемента, съхраняващ данни за
изговорените от абоната минути в различните зони за таксуване – национални, зона 1,
зона 2 и зона 3).
• Информацията за абонатите на мобилния оператор се съхранява във файл в JSON формат,
като не могат да се дублират данни с еднакви клиентски и телефонен номер.

• Дефинирайте функции за:
    ◦ Четене и запис на данните във файл с указано име
    ◦ Добавяне на абонат в списъка
    ◦ Изтриване на абонат в списъка
    ◦ Търсене на абонат по име
    ◦ Търсене на абонат по абонатен номер
    ◦ Отпечатване броя на телефонните номера, регистрирани към абонаментен номер
    ◦ Отпечатване на информация в табличен вид със следните колони: Клиентски N, Телефонен N, Име на клиента, национални, зона 1, зона 2, зона 3

В главната програма създайте меню, чрез което потребителят да изпълнява определена функционалност от разработената програмата.
'''

import json
from typing import List

class Client:
    def __init__(self, client_number, phone_number, name, calls):
        self.client_number = client_number
        self.phone_number = phone_number
        self.name = name
        self.calls = calls

    def __str__(self):
        return f'{self.client_number} {self.phone_number} {self.name} {self.calls}'
    
    def __repr__(self):
        return f'{self.client_number} {self.phone_number} {self.name} {self.calls}'
    
    def __eq__(self, other):
        return self.client_number == other.client_number and self.phone_number == other.phone_number
    
    def __hash__(self):
        return hash(self.client_number + self.phone_number)
    
    def to_dict(self):
        return {
            'client_number': self.client_number,
            'phone_number': self.phone_number,
            'name': self.name,
            'calls': self.calls
        }
    
    @staticmethod
    def from_dict(d):
        return Client(d['client_number'], d['phone_number'], d['name'], d['calls'])
    
    def add_call(self, call):
        self.calls.append(call)

def read_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        return [Client.from_dict(d) for d in data]
    
def write_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump([c.to_dict() for c in data], file, indent=4)

def add_client(data, client):
    if client in data:
        return False
    data.append(client)
    return True

def delete_client(data, client_number):
    for client in data:
        if client.client_number == client_number:
            data.remove(client)
            return True
    return False

def search_by_name(data, name):
    return [c for c in data if name in c.name]

def search_by_client_number(data, client_number):
    return [c for c in data if c.client_number == client_number]

def print_phone_numbers(data, client_number):
    return len([c for c in data if c.client_number == client_number])

def print_table(data):
    print(f'Клиентски N\tТелефонен N\tИме\tНационални\tЗона 1\tЗона 2\tЗона 3')
    for c in data:
        print(f'{c.client_number}\t\t{c.phone_number}\t{c.name}\t{c.calls[0]}\t{c.calls[1]}\t{c.calls[2]}\t{c.calls[3]}')

def main():
    file_name: str = input('Enter file name (task10_clients.json): ')
    if not file_name:
        file_name = 'task10_clients.json'

    try:
        data: List[Client] = read_data(file_name)
    except:
        data = []

    while True:
        print('1. Add client')
        print('2. Delete client')
        print('3. Search by name')
        print('4. Search by client number')
        print('5. Print phone numbers count')
        print('6. Print table')
        print('7. Read file')
        print('8. Save')
        print('9. Save and Exit')
        
        choice = input('Enter choice: ')
        
        if choice == '1': # V
            client_number = input('Enter client number: ')
            phone_number = input('Enter phone number: ')
            name = input('Enter name: ')
            calls = []
            for i in range(4):
                calls.append(int(input(f'Enter calls for zone {'national' if i == 0 else i}: ')))
            client = Client(client_number, phone_number, name, calls)
            if add_client(data, client):
                print('Client added')
            else:
                print('Client already exists')
        elif choice == '2': # V
            client_number = input('Enter client number: ')
            if delete_client(data, client_number):
                print('Client deleted')
            else:
                print('Client not found')
        elif choice == '3': # V
            name = input('Enter name: ')
            found_clients = search_by_name(data, name)
            print_table(found_clients)
        elif choice == '4': # V
            client_number = input('Enter client number: ')
            clients = search_by_client_number(data, client_number)
            print_table(clients)
        elif choice == '5': # V
            client_number = input('Enter client number: ')
            print(print_phone_numbers(data, client_number))
        elif choice == '6': # V
            print_table(data)
        elif choice == '7': # V
            file_name = input('Enter file name: ')
            try:
                data = read_data(file_name)
            except:
                print('Error reading file')
                data = []
        elif choice == '8': # V
            write_data(file_name, data)
        elif choice == '9': # V
            write_data(file_name, data)
            break

main()