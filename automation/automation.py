import re

with open('assets/potential-contacts.txt', 'r') as f:
    content = f.read()

def find_phone_numbers():
    cleaned_content = re.findall(r'[(]?[0-9]+[)]?-?[0-9]{3}-?[0-9]{4}',content)
    phone_numbers = []
    for number in cleaned_content:
        if number[3] == '-':
            phone_numbers.append(number)
        if number[0] == '(':
            phone_numbers.append(number[1:4] + '-' + number[5:])
        if len(number) == 10:
            phone_numbers.append(number[0:3] + '-' + number[3:6] + '-' + number[6:])
    phone_numbers = sorted(phone_numbers)
    phone_numbers = list(dict.fromkeys(phone_numbers))
    
    with open('phone_numbers.txt', 'w+') as file:
        for phone in phone_numbers:
            file.write(f'{phone}\n')

find_phone_numbers()

def find_emails():
    cleaned_emails = re.findall(r'[\w.+-_]+@[\w-]+.\w+', content)
    cleaned_emails = sorted(cleaned_emails)

    with open('emails.txt','w+') as file:
        for email in cleaned_emails:
            file.write(f'{email}\n')

find_emails()
   