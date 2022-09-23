alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Программа для шифрования и расширования сообщения методом Цезаря')
x = int(input('Введите 1 для шифровки или 2 для расшифровки сообщения: '))
if x == 1:
    step = int(input('Шаг шифровки: '))
    message = input('Введите сообщение на английском языке для шифровки: ').upper()
    result = ''
        
    for i in message:
        position = alphabet.find(i)
        new_position = position + step
        if i in alphabet:
            result += alphabet[new_position]
        else:
            result += i 
    print ('Ваше зашифрованное сообщение:', result)

elif x == 2:
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
    
else:
    print('Вы ввели неправильную команду. Повторите попытку.')
