def choose_options():
    options = ('piedra','papel','tijera')
    user_option = input('piedra papel o tijera =>')
    user_option.lower()

    if not user_option in options:
        print('Esa opcion no es valida')
        #continue
        return None,None

    computer_option = random.choice(options)


    print('User Choice =>', user_option)
    print('Computer Choice =>', computer_option)
    return user_option,computer_option
