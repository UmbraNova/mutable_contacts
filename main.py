contacts = dict()

while True:
    print('='*40, '\nEnter action[1 or 2]: ')
    print('1. «Add contact»\n2. «Find contact»\n', '-'*20)
    action = input('--> ')
    print('-'*20)

    if action == '1':
        name = tuple(input('\tEnter name and surname: ').split())
        phone = int(input('\tEnter phone number: '))
        if len(name) < 2:
            print('\n\t[Wrong input! Input should look like "Name Surname"]\n')
            continue
        if name in contacts:
            print('\t[You already have this contact in your contact list.]\n', )
            continue
        contacts[name] = phone
        print(f'\n\tCurrent contacts: {contacts}\n')

    elif action == '2':
        search_name = input('\tEnter surname you want to find: ')
        for i_key in contacts:
            if search_name == i_key[1]:
                print(*i_key, contacts[i_key])
                break
        else:
            print('\n\t[Surname not found!]\n')
    else:
        print('\n\t[Input Error! Try again.]')
