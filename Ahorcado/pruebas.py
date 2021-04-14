import os

'''class Usuario:
    def __init__(self,lifes):   
        self.lifes = lifes

    def loose_lifes (self):
            self.lifes = self.lifes - 1
            print(self.lifes)

def juego(lifes ,word_choosed, count):
    while lifes > 0:
        os.system('clear')
        print("Nivel", count,'                       ', 'vidas:', lifes )
        sym = "_ " * len(word_choosed)
        print(sym)
        if input("respuesta") !=  word_choosed:
            os.system('clear')
            lifes = lifes - 1
        else:
            print('you win')
            break
    if x == 0:
        print('you loose')

    count = count + 1
    print(count)




def run():
    xus = Usuario(3)
    print(xus.lifes)


    juego(xus.lifes,"Hola", 1)


run()'''
def clean():
    os.system('clear')

def to_str(lst):
    word = ""
    for i in lst:
        word += i
        word +=" "
    return word


def stadandar(word):

    repleaced_word = word.maketrans("áéíóú", "aeiou")
    translated_word = word.translate(repleaced_word).upper()
    return(translated_word)

def to_list(word):
    word_2_list = []      
    word_2_list[:0] = word
    return word_2_list

def find_letter(inp_letter,word_2_list):
    order_letter = []
    for i in range(len(word_2_list)):
        if inp_letter == word_2_list[i]:
            order_letter.append(i)


    return order_letter

def dashes(dashes_n,order_letter,word_2_list):

    for i in range(len(word_2_list)):
        for j in range(len(order_letter)):
            if i == order_letter[j]:
                dashes_n[i]=word_2_list[i]

    return(dashes_n)

def juego(lifes, word_choosed, count):
    dashes_n = to_list("_" *len(word_choosed))
    word = stadandar(word_choosed)
    word_lst = to_list(word)

    while dashes_n != word_lst:
        clean()
        print('Nivel', count, '                      ',
        "vidas", lifes)
        print(to_str(dashes_n))
        letter = input("Inserte una letra: ").upper()
        if letter == "EXIT":
            clean()
            print("Hasta la proxima")
            break
        letter_finded = find_letter(letter, word_lst)
        dashes_n = dashes(dashes_n, letter_finded, word_lst)
        

    clean()
    print(to_str(dashes_n), "Bien Hecho")
    return

    



def run():


    x = stadandar('árbol')
    '''y = to_list(x)
    z = find_letter("A",y)
    das = to_list("_" *len('arbol'))
    a = dashes(das,z,y)'''

    juego(3,'arbol',1)

run() 