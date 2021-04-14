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
                print('already', self.name)
            else :
                f.write(self.name)
                f.write("\n")
                print('new name', self.name)

    def loose_lifes (self, n):
        self.lifes = n
        print(self.lifes)

    def gain_lifes(self, n):
        self.lifes = n
        print(self.lifes)

    def lifes_count(self):
        return(self.lifes)
        

    def score(self):
        pass



def choose_word(lst):
        num = random.randint(0, len(lst))
        choosed = lst[num]
        #print(choosed)
        return(choosed)


def random_words():
    word_lst = []
    with open("./data.txt", 'r', encoding="utf-8") as f:
        for word in f:
            word_lst.append(word.replace("\n", ""))   
    return(word_lst)

def juego(lifes ,word_choosed, count):
    n = lifes
    while n > 0:
        os.system('clear')
        print(word_choosed)
        print("Nivel", count,'                       ', 'vidas:', n )
        sym = "_ " * len(word_choosed)
        print(sym)
        if input("respuesta") in  word_choosed:
            os.system('clear')
            n = n - 1
        else:
            print('you win')
            count = count + 1
            break
    if n == 0:
        print('you loose')

    
    return(count, n)


def run():
    os.system('clear')
    nm = input('Enter your name: ')
    assert len(nm) < 7, "Name can't be more than 6 character length"
    user = Usuario(nm.upper(), 3)
    user.user_name()
    print(user.lifes)
    word_lst_rdm = random_words ()
    word_choosed = choose_word(random_words())
    print(word_choosed)


    while user.lifes > 0:
        user.loose_lifes(juego(user.lifes, choose_word(random_words()), 1)[1])
    

    


run()