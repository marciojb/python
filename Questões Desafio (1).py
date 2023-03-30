#desafio
camião  = int(input('quantos caminhões voce tem? '))
for number in range(camião):
 while True:
    try:
        peso_Carga  = float(input('qual e o peso da carga? '))
        break
    except ValueError:
        print('Não foi digitado um número')
 tonelada = peso_Carga * 1.000
 while True :
    try:
        codigo_estado = int(input('qual e seu codigo do estado? '))
        if codigo_estado >= 1 and codigo_estado <=5:
            break
        print('digite um numero 1 a 5')
    except ValueError:
        print('Não foi digitado um número')
 while True:
    try:
        codigo_Carga = int(input('qual e seu codigo de carga? '))
        if codigo_Carga >= 10 and codigo_Carga <= 40:
            break
        print('digite um numero 10 a 40')
    except ValueError:
        print('Não foi digitado um número')
 if codigo_Carga >= 10 and codigo_Carga <= 19 :
     preço1 = (tonelada * 100)
     print(' O preço da carga foi : %5.2f' % preço1, 'R$')
 if codigo_Carga >= 20 and codigo_Carga <= 29 :
     preço2= (tonelada * 250)
     print(' O preço da carga foi : %5.2f' % preço2, 'R$')
 if codigo_Carga >=30 and codigo_Carga<= 40 :
    preço3= (tonelada * 340)
    print(' O preço da carga foi : %5.2f' % preço3, 'R$')
 print('tonelada para kilo:  %3.3f ' %tonelada ,'KG')
 while True:
    try:
        if codigo_estado == 1:
            imposto1 = preço1 * (35 / 100)
            print('imposto em cima da carga : %5.2f'%imposto1,'R$')
            total_caminhão = imposto1 + preço1
            print('total do caminhão foi:  %5.2f'%total_caminhão,'R$' )
        if codigo_estado == 2:
            imposto2 = preço1 * (25 / 100)
            print('imposto em cima da carga : %5.2f'%imposto2,'R$')
            total_caminhão1 = imposto2 + preço1
            print('total do caminhão foi:  %5.2f'%total_caminhão1,'R$' )
        if codigo_estado == 3:
            imposto3 = preço1 * (15 / 100)
            print('imposto em cima da carga : %5.2f'%imposto3,'R$')
            total_caminhão2 = imposto3 + preço1
            print('total do caminhão foi:  %5.2f'%total_caminhão2,'R$' )
        if codigo_estado == 4:
            imposto4 = preço1 * (5 / 100)
            print('imposto em cima da carga : %5.2f'%imposto4,'R$')
            total_caminhão3 = imposto4 + preço1
            print('total do caminhão foi:  %5.2f' % total_caminhão3, 'R$')
        if codigo_estado == 5:
            imposto5= preço1 * 0
            print('imposto em cima da carga : %5.2f' % imposto5, 'R$')
            total_caminhão4 = imposto5 + preço1
            print('total do caminhão foi:  %5.2f' % total_caminhão4, 'R$')
        break
    except NameError :
        break
 while True:
    try:
        if codigo_estado == 1:
            imposto1 = preço2 * (35 / 100)
            print('imposto em cima da carga : %5.2f' % imposto1, 'R$')
            total_caminhão = imposto1 + preço2
            print('total do caminhão foi:  %5.2f' % total_caminhão, 'R$')
        if codigo_estado == 2:
            imposto2 = preço2 * (25 / 100)
            print('imposto em cima da carga : %5.2f' % imposto2, 'R$')
            total_caminhão1 = imposto2 + preço2
            print('total do caminhão foi:  %5.2f' % total_caminhão1, 'R$')
        if codigo_estado == 3:
            imposto3 = preço2 * (15 / 100)
            print('imposto em cima da carga : %5.2f' % imposto3, 'R$')
            total_caminhão2 = imposto3 + preço2
            print('total do caminhão foi:  %5.2f' % total_caminhão2, 'R$')
        if codigo_estado == 4:
            imposto4 = preço2 * (5 / 100)
            print('imposto em cima da carga : %5.2f' % imposto4, 'R$')
            total_caminhão3 = imposto4 + preço2
            print('total do caminhão foi:  %5.2f' % total_caminhão3, 'R$')
        if codigo_estado == 5:
            imposto5 = preço2 * 0
            print('imposto em cima da carga : %5.2f' % imposto5, 'R$')
            total_caminhão4 = imposto5 + preço2
            print('total do caminhão foi:  %5.2f' % total_caminhão4, 'R$')

        break
    except NameError :
        break
 while True:
    try:
        if codigo_estado == 1:
            imposto1 = preço3 * (35 / 100)
            print('imposto em cima da carga : %5.2f' % imposto1, 'R$')
            total_caminhão = imposto1 + preço3
            print('total do caminhão foi:  %5.2f' % total_caminhão, 'R$')
        if codigo_estado == 2:
            imposto2 = preço3 * (25 / 100)
            print('imposto em cima da carga : %5.2f' % imposto2, 'R$')
            total_caminhão1 = imposto2 + preço3
            print('total do caminhão foi:  %5.2f' % total_caminhão1, 'R$')
        if codigo_estado == 3:
            imposto3 = preço3 * (15 / 100)
            print('imposto em cima da carga : %5.2f' % imposto3, 'R$')
            total_caminhão2 = imposto3 + preço3
            print('total do caminhão foi:  %5.2f' % total_caminhão2, 'R$')
        if codigo_estado == 4:
            imposto4 = preço3 * (5 / 100)
            print('imposto em cima da carga : %5.2f' % imposto4, 'R$')
            total_caminhão3 = imposto4 + preço3
            print('total do caminhão foi:  %5.2f' % total_caminhão3, 'R$')
        if codigo_estado == 5:
            imposto5 = preço3 * 0
            print('imposto em cima da carga : %5.2f' % imposto5, 'R$')
            total_caminhão4 = imposto5 + preço3
            print('total do caminhão foi:  %5.2f' % total_caminhão4, 'R$')
        break
    except NameError :
     break