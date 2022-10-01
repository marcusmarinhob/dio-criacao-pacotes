from sum import sum_op
from sub import sub_op
from mult import multi_op
from div import div_op

print("Calculadora ")
print("*"*20)
print("A - Adição")
print("S - Subtração")
print("M - Multiplicação")
print("D - Divisão\n")

op = input("Digite a operação desejada: ")
a = int(input("Agora digite o valor do primeiro operador: "))
b = int(input("Finalmente digite o valor do segundo operador: "))

match op:
    case 'A':
        op_name, operation = ('adição', sum_op)
    case 'S':
        op_name, operation = ('subtração', sub_op)
    case 'M':
        op_name, operation = ('multiplicação', multi_op)
    case 'D':
        op_name, operation = ('divisão', div_op)
        
res = operation(a, b)

print(f"\nO resultado da {op_name} é {res}")
