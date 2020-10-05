import sys

with open(sys.argv[1], mode='r', encoding='utf-8') as file:
    lines = file.read()

i = 0
result = ''
while i < len(lines):
    if lines[i].isalpha():
        result += lines[i]
        i += 1
        while i < len(lines) and lines[i].isalnum():
            result += lines[i]
            i += 1
        if result == 'BEGIN':
            print('Begin')
        elif result == 'END':
            print('End')
        elif result == 'FOR':
            print('For')
        elif result == 'IF':
            print('If')
        elif result == 'THEN':
            print('Then')
        elif result == 'ELSE':
            print('Else')
        else:
            print('Ident(' + result + ')')
    elif lines[i].isdigit():
        result += lines[i]
        i += 1
        while i < len(lines) and lines[i].isdigit():
            result += lines[i]
            i += 1
        print('Int(' + result.lstrip('0') + ')')
    elif lines[i] == ':':
        i += 1
        if lines[i] == '=':
            i += 1
            print('Assign')
        else:
            print('Colon')
    elif lines[i] == '+':
        print('Plus')
        i += 1
    elif lines[i] == '*':
        print('Star')
        i += 1
    elif lines[i] == ',':
        print('Comma')
        i += 1
    elif lines[i] == '(':
        print('LParenthesis')
        i += 1
    elif lines[i] == ')':
        print('RParenthesis')
        i += 1
    elif lines[i] == ' ' or lines[i] == '\n':
        i += 1
    else:
        break
    result = ''
