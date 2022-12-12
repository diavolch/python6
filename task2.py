'''Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.
5 + 6 * 2 - 3 * 4 / 2
*Пример:*
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
Добавьте возможность использования скобок, меняющих приоритет операций.
'''

ln_in = input('Введите выражение: ').split()

def check(args):
    if '(' in args:
        a = args.index('(')
        b = args.index(')')
        for i in range(a+1,b):
            if args[i] == '(':
                a = i
        return a , b 
    else:
        return False

def aka_eval(args):
    while len(args) != 1:
        while '*' in args or '/' in args:
            try:
                prod_index = args.index('*')
            except:
                prod_index = 100

            try:
                div_index = args.index('/')
            except:
                div_index = 100
            
            if prod_index < div_index:
                args[prod_index-1] = float(args[prod_index-1])*float(args[prod_index+1])
                args.pop(prod_index+1)
                args.pop(prod_index)
            else:
                args[div_index-1] = float(args[div_index-1])/float(args[div_index+1])
                args.pop(div_index+1)
                args.pop(div_index)

        while '+' in args or '-' in args:
            try:
                sum_index = args.index('+')
            except:
                sum_index = 100

            try:
                deg_index = args.index('-')
            except:
                deg_index = 100
                
            if sum_index < deg_index:
                args[sum_index-1] = float(args[sum_index-1])+float(args[sum_index+1])
                args.pop(sum_index+1)
                args.pop(sum_index)

            else:
                args[deg_index-1] = float(args[deg_index-1])-float(args[deg_index+1])
                args.pop(deg_index+1)
                args.pop(deg_index)

    return(args[0])


lst = check(ln_in)

while lst:
    lst2 = ln_in[lst[0] + 1: lst[1]]
    num = aka_eval(lst2)
    ln_in[lst[0]] = str(num)
    del ln_in[lst[0] + 1: lst[1] + 1]
    lst = check(ln_in)

print(aka_eval(ln_in))
