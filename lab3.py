print('Программа для шифрования и расширования сообщения методом Цезаря')
while True:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' #Удвоенный английский алфавит, если сдвиг будет большим
    try:
        x = int(input('Введите 1 для шифровки или 2 для расшифровки сообщения: '))
    except:
        print ('Вы ввели неправильную команду. Повторите попытку.')
        break
    if x == 1: #Функция шифровки
        step = int(input('Введите шаг шифровки диапозоном с 1 до 25: '))
        message = input('Введите сообщение на английском языке для шифровки: ').upper()
        result = ''
        if step > 25: #Если шаг будет превышать 25
            print ('Шаг превысил диапозон. Попробуйте еще раз.')
            break
        for i in message: #Поиск символа в алфавите
            position = alphabet.find(i) #Находим место символа в списке
            new_position = position + step #Сдвиг символа 
            if i in alphabet:
                result += alphabet[new_position]
            else:
                result += i 
        if message = result: #Сравниваем введенный текст пользователя с результатом цикла 
            print ('Вы ввели символ или текст не на английском языке. Попробуйте еще раз.')
        else:
            print ('Ваше зашифрованное сообщение:', result)

    elif x == 2: #Функиция расшифровки
        step = int(input('Введите шаг шифровки диапозоном с 1 до 25: '))
        message = input('Введите сообщение на английском языке для расшифровке: ').upper()
        result = ''
        if step > 25:
            print ('Шаг превысил диапозон. Попробуйте еще раз.')
            break
        for i in message:
            position = alphabet.find(i)
            new_position = position - step
            if i in alphabet:
                result += alphabet[new_position]
            else:
                result += i
        if message == result:
            print ('Вы ввели символ или текст не на английском языке. Попробуйте еще раз.')
        else:
            print ('Ваше зашифрованное сообщение:', result)
    else: #Если неправильно ввели команду
        print('Вы ввели неправильную команду. Повторите попытку.')
    break
