if __name__ == '__main__':
    N = int(input())
    my_list = []
    for itr in range(N):
        input_strings = input().strip().split()
        if input_strings[0] == "print":
            print(my_list)
        elif(input_strings[0] == "sort"):
            my_list.sort()
        elif input_strings[0] == "reverse":
            my_list.reverse()
        elif input_strings[0] == "pop":
            my_list.pop(-1)
        elif input_strings[0] == "append":
            my_list.append(int(input_strings[1]))
        elif input_strings[0] == "insert":
            my_list.insert(int(input_strings[1]), int(input_strings[2]))
        elif input_strings[0] == "remove":
            my_list.remove(int(input_strings[1]))