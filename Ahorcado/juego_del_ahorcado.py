import random
import os

class Usuario:
    def __init__(self, name, lifes):   
        self.name = name
        self.lifes = lifes

    def user_name (self):
        count = 0
        #print('lst',lst)
        with open("./usuarios.txt", 'r+', encoding="utf-8") as f:
            for line in f:
                #print(line)
                if line.strip() == self.name:
                    count = 1
            if count == 1:
                print('Hola', self.name)
            else :
                f.write(self.name)
                f.write("\n")
                print('Bienvenido', self.name)

    '''def loose_lifes (self, n):
        self.lifes = n
        print(self.lifes)

    def gain_lifes(self, n):
        self.lifes = n
        print(self.lifes)

    def lifes_count(self):
        return(self.lifes)
        

    def score(self):
        pass'''


def clean():
    os.system('clear')

def to_str(lst):
    word = ""
    for i in lst:
        word += i
        word +=" "
    return word


def choose_word(lst):
        num = random.randint(0, len(lst))
        choosed = lst[num]
        #print(choosed)
        return(choosed)


def order_words():
    word_lst = []
    with open("./data.txt", 'r', encoding="utf-8") as f:
        for word in f:
            word_lst.append(word.replace("\n", ""))   
    return(word_lst)


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


def play(score, word_choosed, count):
    dashes_n = to_list("_" *len(word_choosed))
    word = stadandar(word_choosed)
    word_lst = to_list(word)


    while dashes_n != word_lst:
       
        clean()
        print('Nivel', count, '                      ',
        "Puntuación: ", score)
        print("\n")
        print(to_str(dashes_n))
        print("\n")
        letter = input("Inserte una letra: ").upper()
        print("\n")
        print("\n")
        print('Puedes escribir exit para terminar la partida.')
        assert letter != "EXIT", "Hasta la proxima"
        '''if letter == "EXIT":
            clean()
            print("Hasta la proxima")
            break'''
        letter_finded = find_letter(letter, word_lst)
        lifes = letter_finded
        dashes_n = dashes(dashes_n, letter_finded, word_lst)
        
    clean()
    print("\n")print("\n")print("\n")
    print(to_str(dashes_n), "Buen Trabajo!!!!!")
    print("\n")
    print("\n")
    input("Presiona Enter para continuar")

    count = count + 1
    score = score + len(word)
    return count, score


def run():

    os.system('clear')
    nm = input('¿Cual es tu nombre?: ')
    assert len(nm) < 7, "Name can't be more than 6 character length"
    clean()
    print("\n")
    print("Bienvenido", nm )
    print("\n")
    print("\n")
    input("Presiona Enter para iniciar")
    user = Usuario(nm.upper(), 3)
    user.user_name()
    orded = order_words()
    count = [1, 1]
    
    for i in range(len(orded)):
        count = play(
            int(count[1]), 
            choose_word(order_words()), 
            int(count[0])
            )
        
    
if __name__ == '__main__':

    run()