def jogo_da_velha():
    print('JOGO DA VELHA')
    player1 = 'X'
    player2 = 'Y'

    escolha = int(input('Digite a sua escolha'))
    escolhas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'''
        


        +=====+=====+=====+
        | {escolhas[0]}   | {escolhas[1]}   | {escolhas[2]}   |
        |     |     |     |
        +=====+=====+=====+
        | {escolhas[3]}   | {escolhas[4]}   | {escolhas[5]}   |
        |     |     |     |
        +=====+=====+=====+
        | {escolhas[6]}   | {escolhas[7]}   | {escolhas[8]}   |
        |     |     |     |
        +=====+=====+=====+
    
    ''')



jogo_da_velha()
