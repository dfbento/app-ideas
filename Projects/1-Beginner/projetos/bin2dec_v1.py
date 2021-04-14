"""
Programa para conversão de número binário para decimal.

"""


def bin2dec(num):
    tamanho = False

    if 8 >= len(num) >= 0:
        tamanho = True
    else:
        print('A quantidade máxima eh 8.')

    if tamanho:
        binario = False
        lista = list()

        for i in num:
            if i != '0' and i != '1':
                print(f'O número digital não é binario.')
                break
            else:
                lista.append(int(i))
                binario = True

        if binario:
            soma = 0
            pos_inicial = len(num)
            for *_, i in enumerate(lista):
                pos_inicial -= 1
                acum = i * (2 ** pos_inicial)
                soma = soma + acum
            print(f'A conversão do número binário "{num}" é equivalente ao "{soma}" decimal.')


while True:
    num = input('Informe um número binário (base 2): ')
    bin2dec(num)
    sair = input('Deseja continuar? [S]im ou [N]ão:')
    if sair == 'N':
        break
