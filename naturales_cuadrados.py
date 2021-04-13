def run():
    lst_height = list(range(int(input('Number of elements:')) + 1))
    lst = []
    for i in lst_height:
        if i == 0:
            continue
        else:
            lst.append(i**2)
    print(lst)



if __name__ == '__main__':
    run()