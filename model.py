phone_book = []
def get_phone_book():
    global phone_book
    return phone_book

def open_file():
    global phone_book
    with open('phone_book.txt', 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))
    print(phone_book)

def save_file():
    global phone_book
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open('phone_book.txt', 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))
        
def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)
    
def get_contact(text: str):
    global phone_book
    result = []
    for i, contact in enumerate(phone_book):
        for field in contact:
            if text in field:
                result.append((contact, i))
    if len(result) > 1:
        return False
    else:
        return result
               
def change_contact(index: int, new: list):
    global phone_book
    phone_book[index][0] = new[0] if new[0] != '' else phone_book[index][0]
    phone_book[index][1] = new[1] if new[1] != '' else phone_book[index][1]
    phone_book[index][2] = new[2] if new[2] != '' else phone_book[index][2]
    
def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def delete_contact(contact: list):
    global phone_book
    phone_book.remove(contact)