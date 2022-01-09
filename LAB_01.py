with open('test.txt') as f:
    lines = f.read().replace(',', ' ,').replace(';', ' ;')
f.close()

keywords = ["auto", "break", "case", "char", "const", "continue", "default",
            "do", "double", "else", "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return", "short", "signed",
            "sizeof", "static", "struct", "switch", "typedef", "union",
            "unsigned", "void", "volatile", "while"];

num = []
others = []
math = []
logic = []
identi = []
key = []
a = False

for ch in lines.split():

    try:
        float(ch)
        a = True
    except ValueError:
        a = False

    if (ch.isnumeric()) or a == True:
        if ch not in num:
            num.append(ch)
    elif (ch == '.' or ch == ',' or ch == ';' or ch == '(' or ch == ')' or ch == '{' or ch == '}'):
        if ch not in others:
            others.append(ch)
    elif (ch == '+' or ch == '-' or ch == '=' or ch == '*' or ch == '/' or ch == '%'):
        if ch not in math:
            math.append(ch)
    elif (ch == '>' or ch == '<' or ch == '&&' or ch == '||*' or ch == '!' or ch == '%'):
        if ch not in logic:
            logic.append(ch)
    elif ch in keywords:
        if ch not in key:
            key.append(ch)
    else:
        if ch not in identi:
            identi.append(ch)

print('Keywords:', end=' ')
print(*key, sep=', ')
print('Identifiers:', end=' ')
print(*identi, sep=', ')
print('Math Operators:', end=' ')
print(*math[::-1], sep=', ')
print('Logical Operators:', end=' ')
print(*logic, sep=', ')
print('Numerical Values:', end=' ')
print(*num, sep=', ')
print('Others:', *others)
