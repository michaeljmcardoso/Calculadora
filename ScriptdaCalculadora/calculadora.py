def bemvindo():
    print('''Bem-vindo à Calculadora''')

def calcular():
    operação = input('''
Digite a operação matemática que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
% para resto da divisão
** para potenciação
''')

    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))

    if operação == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)
    elif operação == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)
    elif operação == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)
    elif operação == '/':
        print('{} / {} '.format(numero_1, numero_2))
        print(numero_1 / numero_2)
    elif operação == '%':
        print('{} % {} '.format(numero_1, numero_2))
        print(numero_1 % numero_2)
    elif operação == '**':
        print('{} ** {} '.format(numero_1, numero_2))
        print(numero_1 ** numero_2)
    else:
        print('Você não digitou um operador válido, por favor execute o programa outra vez! ')
    # Adicionar novamente() função para calcular() função
    calcnovamente()

def calcnovamente():
    calcule_novamente = input('''
Você quer calcular novamente?
Por favor, digite S para SIM ou N para NÃO.
''')
    # Se o usuário digitar Y, execute a função calcular()
    if calcule_novamente.upper() == 'S':
        calcular()
    # Se o usúario digitar N, diga até mais para o usuário e feche o programa
    elif calcule_novamente.upper() == 'N':
        print('Até mais! ')
    else:
        calcnovamente()

bemvindo()
calcular()
