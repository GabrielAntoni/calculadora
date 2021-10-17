def arqres(N1,N2,eq,res):
    arquivo = open('rescalculadora.txt','a')
    if eq == '%':
        arquivo.write(f'{N2}% de {N1} = {res}'+'\n')
    elif eq.upper() == 'R':
        arquivo.write(f'{N2} raiz de {N1} = {res}'+'\n')
    else:
        arquivo.write(f'{N1} {eq} {N2} = {res}'+'\n')
    arquivo.close()
def abrres():
    arquivo = open('rescalculadora.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()
def soma(N1,N2):
    return N1 + N2
def sub(N1,N2):
    return N1 - N2
def mult(N1,N2):
    return N1 * N2
def div(N1,N2):
    return N1 /N2
def poten(N1,N2):
    return N1**N2
def restdiv(N1,N2):
    return N1 % N2
def porcent(N1,N2):
    return (N1*N2)/100
def raiz (N1,N2):
    return N1**(1/N2)

def bem_vindo():
    print('*' * 36)
    print('**** Bem vindo a calculadora!!! ****')
    print('*' * 36)
def calculadora():
    try:
        N1 = float(input('coloque o primeiro numero: '))
        N2 = float(input('coloque o sugundo numero: '))
    except ValueError:
        print('coloque apenas numeros.')
        calculadora()
    eq = input('''coloque um simbolo simples para a operação:
Subitração = (-)
Soma = (+)
Multplicação = (*) 
Divisão = (/)
Potencia = (**)
Resto de uma divisão ou modulo = (M) 
Porcentagem = (%)
Raiz = (R)
 ''')


    if eq == '-':
        res = sub(N1,N2)
        print(f'o resultado é: {N1} - {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '+':
        res = soma(N1,N2)
        print(f'o resultado é: {N1} + {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '*':
        res = mult(N1,N2)
        print(f'o resultado é: {N1} * {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '/'and N2 != 0:
        res = div(N1,N2)
        print(f'o resultado é: {N1} / {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '**':
        res =poten(N1,N2)
        print(f'o resultado é: {N1} ** {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq.upper() == 'M':
        res = restdiv(N1,N2)
        print(f'o resultado é: {N1} M {N2} = {res}')
        arqres(N1,N2,eq,res)
    elif eq == '%':
        res = porcent(N1,N2)
        print(f'o resultado é: {N2}% de {N1} = {res}')
        arqres(N1,N2,eq,res)
    elif eq.upper() == 'R':
        res = raiz(N1, N2)
        print(f'o resultado é: {N2} raiz de {N1} = {res}')
        arqres(N1,N2,eq,res)
    else:
        print('operação invalida tente novamente')

    repetir()

def repetir():
    calc_repetir = input('''
você deseja fazer outro calculo?
Se sim coloque S para Sim 
Se não deseja coloque N para NÃO
se desejar ver todos os resultados coloque RES
''')
    if calc_repetir.upper() == 'S':
        calculadora()
    elif calc_repetir.upper() == 'N':
        print('Até depois.')
    elif calc_repetir.upper() == 'RES':
        abrres()
        repetir()
    else:
        repetir()
