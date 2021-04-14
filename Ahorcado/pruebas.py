import os

class Usuario:
    def __init__(self,lifes):   
        self.lifes = lifes

    def loose_lifes (self):
            self.lifes = self.lifes - 1
            print(self.lifes)

def juego(x,word_choosed, count):
    while x > 0:
        os.system('clear')
        print("Nivel", count,'                   ', 'vidas:', x )
        sym = "_ " * len(word_choosed)
        print(sym)
        if input("respuesta") !=  word_choosed:
            os.system('clear')
            x = x - 1
        else:
            print('you win')
            print(xus.lifes)
            break
    if x == 0:
        print('you loose')

    count = count + 1
    print(count)


def run():
    xus = Usuario(3)
    print(xus.lifes)


    juego(xus.lifes,"Hola", 1)


run()
