def run():

    ### numeros de 1 a n, en un dict, donde k = n y v = n**2, mi version
    #ran = int(input('range: '))
    #lst = range(ran)
    #nat_nums = dict(zip([i for i in lst[1:]], [j**3 for j in lst[1:] ]))
    #for v,k in nat_nums.items():
    #    print(v, '^2:', k)

    # version del profesor
    #my_dict = {}
    #for i in range(1, 101):
    #    my_dict[i] = i ** 3
    #print(my_dict)

    #RETO
    my_dict = {}
    for i in range(1, 101):
        if i%3 != 0:
            my_dict[i] = i ** 3
    print(my_dict)

if __name__ == '__main__':
    run()