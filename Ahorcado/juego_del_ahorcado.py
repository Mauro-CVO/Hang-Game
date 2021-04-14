import random
import os

class Usuario:
    def __init__(self, name):   
        self.name = name

    def user_name (self):
        lst = []
        lst.append(self.name)
        count = 0
        #print('lst',lst)
        with open("./usuarios.txt", 'r+', encoding="utf-8") as f:
            for line[:5] in f:
                #print(line)
                if line.strip() == self.name:
                    count = 1
            if count == 1:
                print('already', self.name)
            else:
                #f.write("\n")
                f.write(self.name)
                f.write("\n")
                print('new name', self.name)

    def loose_lifes (self):
        vida = vida - 1
    
    def gain_lifes(self):
        vida = vida + 1

    def score(self):
        pass



def choose_word(lst):
        num = random.randint(0, len(lst))
        choosed = lst[num]
        print(choosed)


def random_words():
    word_lst = []
    with open("./data.txt", 'r', encoding="utf-8") as f:
        for word in f:
            word_lst.append(word.replace("\n", ""))   
    return(word_lst)



def run():
    os.system('clear')
    name = input('Enter your name: ').upper
    assert len(nm) < 7, "Name can't be more than 6 character length"
    
    user = Usuario(name)
    user.user_name()

    x = random_words ()
    w = choose_word(x)
    

run()