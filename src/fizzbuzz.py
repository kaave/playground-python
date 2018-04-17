def fizzbuzz():
    for index in range(1, 100 + 1):
        is_fizz = index % 3 == 0
        is_buzz = index % 5 == 0

        if is_fizz and is_buzz:
            print('fizzbuzz', end='')
        elif is_fizz:
            print('fizz', end='')
        elif is_buzz:
            print('buzz', end='')
        else:
            print(index, end='')

        if index >= 10 and index % 10 == 0:
            print('')
        else:
            print(' ', end='')


fizzbuzz()
