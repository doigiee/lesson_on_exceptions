while True:
    try:
        x = get_int()
        print( 1 / x)
        break
    except ValueError as err:
        print(err.args)
        print('Input must be an integer')
    except ZeroDivisionError:
        print('Input cannot be zero')

print(f'You entered {x}')