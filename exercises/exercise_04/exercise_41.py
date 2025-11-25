def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print(f'{a}/{b}\nError: Can not divide by zero!')
    except ValueError:
        print(f'{a}/{b}\nError: Invalid value')
    except TypeError:
        print(f'{a}/{b}\nError: Invalid input type. Please provide numbers')
    else:
        print(f'{a}/{b} = {result}\nDivision successful!')
    finally:
        print("Operation complete.")


print(f'Test 1: ')
safe_divide(10,2)

print(f'Test 2: ')
safe_divide(10,0)

print(f'Test 3: ')
safe_divide(10,"abc")

