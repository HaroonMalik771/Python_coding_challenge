if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    values = [
        [value1, value2, value3]
        for value1 in range(x+1)
        for value2 in range(y+1)
        for value3 in range(z+1)
        if(value1 + value2 + value3) != n
    ]
    print(values)