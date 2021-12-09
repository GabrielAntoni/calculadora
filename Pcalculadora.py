def invalido ():
    print('comando invalido')
    repetir()
def arqres(N1,N2,eq,res):
    arquivo = open('rescalculadora.txt','a')
    if eq == '%':
        arquivo.write(f'{N2}% de {N1} = {res}'+'\n')
    elif eq.upper() == 'R':
        arquivo.write(f'raiz de {N1} = {res}'+'\n')
    elif eq.upper() == "B":
        arquivo.write(f'o numero {N1} em binario é = {res}'+'\n')
    else:
        arquivo.write(f'{N1} {eq} {N2} = {res}'+'\n')
    arquivo.close()
def numeros():
    try:
        N1 = float(input('coloque o primeiro numero: '))
        N2 = float(input('coloque o sugundo numero: '))
    except ValueError:
        print('coloque apenas numeros.')
        numeros()
    return N1,N2
def numero():
    try:
        N1 = int(input('coloque o numero: '))
    except ValueError:
        print('coloque apenas numeros sem pontuação.')
        numero()
    return N1
def abrres():
    arquivo = open('rescalculadora.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()
def binario(N1):
    b = ''
    while N1 > 0:
        b += str(int(N1) % 2)
        N1 = N1 // 2
    return b[::-1]
def soma(N1,N2):
    return N1 + N2
def sub(N1,N2):
    return N1 - N2
def mult(N1,N2):
    return N1 * N2
def div(N1,N2):
    return N1 / N2
def poten(N1,N2):
    return N1**N2
def restdiv(N1,N2):
    return N1 % N2
def porcent(N1,N2):
    return (N1*N2)/100
def raiz (N1):
    return N1**(1/2)

def bem_vindo():
    print('*' * 36)
    print('**** Bem vindo a calculadora!!! ****')
    print('*' * 36)
def calculadora():
    eq = input('''coloque um simbolo simples para a operação:
Subitração = (-)
Soma = (+)
Multplicação = (*) 
Divisão = (/)
Potencia = (**)
Resto de uma divisão ou modulo = (M) 
Porcentagem = (%)
Raiz = (R)
converter em binario (B)
''')


    if eq == '-':
        N1,N2 = numeros()
        res = sub(N1,N2)
        print(f'o resultado é: {N1} - {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '+':
        N1, N2 = numeros()
        res = soma(N1,N2)
        print(f'o resultado é: {N1} + {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '*':
        N1, N2 = numeros()
        res = mult(N1,N2)
        print(f'o resultado é: {N1} * {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '/':
        N1, N2 = numeros()
        if N2 == 0:
            invalido()
        res = div(N1,N2)
        print(f'o resultado é: {N1} / {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '**':
        N1, N2 = numeros()
        res =poten(N1,N2)
        print(f'o resultado é: {N1} ** {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq.upper() == 'M':
        N1, N2 = numeros()
        res = restdiv(N1,N2)
        print(f'o resultado é: {N1} M {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '%':
        N1, N2 = numeros()
        res = porcent(N1,N2)
        print(f'o resultado é: {N2}% de {N1} = {res}')
        arqres(N1,N2,eq,res)
    elif eq.upper() == 'R':
        N1 = numero()
        res = raiz(N1)
        print(f'o resultado é:raiz de {N1} = {res}')
        arqres(N1,'',eq,res)
    elif eq.upper() == 'B':
        N1 = numero()
        res = binario(N1)
        print(f'o o numero {N1} em binario é = {res}')
        arqres(N1, '', eq, res)
    else:
        print('operação invalida tente novamente')

    repetir()

def repetir():
    calc_repetir = input('''
você deseja fazer outro calculo?
Se sim coloque S para Sim 
Se não deseja coloque N para NÃO
Se desejar ver todos os resultados coloque R
''')
    if calc_repetir.upper() == 'S':
        calculadora()
    elif calc_repetir.upper() == 'N':
        print('Até depois.')
    elif calc_repetir.upper() == 'R':
        abrres()
        repetir()
    else:
        repetir()
