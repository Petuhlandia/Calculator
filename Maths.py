import math

print("Ноль в к качестве знака операции завершит работу программы")
while True:
    s = input("Знак(+,-,*,/,sin,cos,tg):")
    if s == '0': break
    if s in ('+','-','*','/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    elif s in ('cos','sin','tg'):
        x = float(input("x="))
        if s == 'sin':
            print("%.2f" % (math.sin(x)))
        elif s == 'cos':
            print("%.2f" % (math.cos(x)))
        elif s == 'tg':
            print("%.2f" % (math.tan(x)))
    else:
        print("Неверный знак операции!")