alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' #Удвоенный английский алфавит, если сдвиг будет большим
print('Программа для шифрования и расширования сообщения методом Цезаря')
x = int(input('Введите 1 для шифровки или 2 для расшифровки сообщения: '))
if x == 1: #Функция шифровки
    step = int(input('Шаг шифровки: '))
    message = input('Введите сообщение на английском языке для шифровки: ').upper()
    result = ''
        
    for i in message: #Поиск символа в алфавите
        position = alphabet.find(i) #Находим место символа в списке
        new_position = position + step #Сдвиг символа 
        if i in alphabet:
            result += alphabet[new_position]
        else:
            result += i 
    print ('Ваше зашифрованное сообщение:', result)

elif x == 2: #Функиция расшифровки
    step = int(input('Шаг шифровки: '))
    message = input('Введите сообщение на английском языке для расшифровке: ').upper()
    result = ''
    for i in message:
        position = alphabet.find(i)
        new_position = position - step
        if i in alphabet:
            result += alphabet[new_position]
        else:
            result += i
    print ('Ваше расшифрованное сообщениe:', result)
    
else: #Если неправильно ввели команду
    print('Вы ввели неправильную команду. Повторите попытку.')
