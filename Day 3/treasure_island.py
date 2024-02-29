print('Bienvenido a la Isla del Tesoro, tu misión es encontrar el tesoro')
camino_elegido = input('El camino se divide, ¿A donde quieres ir a la derecha o a la izquierda?')
camino_elegido.lower()
if camino_elegido == 'izquierda':
    print('Eres atacado por un grupo de Ogros. GAME OVER')
elif camino_elegido == 'derecha':
    nadar_esperar = input('Llegas a una playa, ¿Qué quieres hacer, esperar o nadar hasta la isla que se ve a lo lejos?')
    nadar_esperar.lower()
    if nadar_esperar == 'nadar':
        print('Al poco rato de estar nadando te atancan tiburones. GAME OVER')
    elif nadar_esperar == 'esperar':
        print('Al poco rato de estar esperando aparece un barco que se ofrece a llevarte a la isla')
    else:
        print('Opción no valida')
        puerta = input('Llegas ante un muro con tres puertas, una roja, una azul y una amarilla. ¿Por cual entras?')
        puerta.lower()
        if puerta == 'roja':
            print('Grandes llamas te abrasan hasta la muerte. GAME OVER')
        elif puerta == 'azul':
            print('Eres devorado por bestias salvajes. GAME OVER')
        elif puerta == 'amarilla':
            print('!Encuentras la sala del tesoro HAS GANADO¡')
        else:
            print('Opción no valida')
else:
    print('Opción no valida')