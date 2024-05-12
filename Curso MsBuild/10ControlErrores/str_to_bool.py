# Create a function (str_to_bool) that converts strings to booleans. The user may input one of the following entries: +, positive, true, y, yes / -, negative, false, n, no.
# The function must convert the variable into te correct boolean data type.

#DEF variables y listas
tValues = ['+', 'positive', 'true', 'y', 'yes']
fValues = ['-', 'negative', 'false', 'n', 'no']  
cValue =  ''

#DEF function
def str_to_bool(val):
    try:
        if val.lower() in tValues:
            return True
        elif val.lower() in fValues:
            return False
        else:
            raise RuntimeError
    except RuntimeError:
        print('Invalid entry.\n')

#Program
while not isinstance(cValue, bool): # evalua si cValue es bool
    value = input('Insert string to convert into boolean: ')
    cValue = str_to_bool(value)
print(f'\n{value} converted to {cValue}')