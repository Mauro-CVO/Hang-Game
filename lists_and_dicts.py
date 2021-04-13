def run():
    #my_list = [1, "Hello", 4.5]
    #my_dict = {"firstname" : "Mauro", "lastname" : "Cortes"}

    super_list = [
        {"firstname" : "Mauro", "lastname" : "Cortes"}, 
        {"firstname" : "Aurora", "lastname" : "Espinal"},
        {"firstname" : "Hector", "lastname" : "Feria"},
        {"firstname" : "Guillermo", "lastname" : "Legorreta"},
    ]

    super_dict = {
        "natural_nums" : [1, 2, 3, 4, 5],
        "int_nums" : [-2, -1, 0, 1, 2],
        "float_nums" : [1.1, 4.5, 6.43]
    }

    for k, v in super_dict.items():
        print(k, '-', v)

    for i in super_list:
        for k,v in i.items():
            print(k, '-', v)

if __name__ == '__main__':
    run()
