if __name__ == '__main__':
    print('Hello\nWorld') # New Line
    print("Hello\tSRK") # Tab

    # Separator attribute
    a,b,c,d = 10,20,30,40
    print(a,b,c,d) # 10 20 30 40
    print(a,b,c,d, sep=':') # 10:20:30:40

    # end attribute
    print('Hello', end=' ')
    print('duga', end=' ')
    print('soft')

    print('Hello',end='::')
    print('durga',end='$$$')
    print('soft')

    # separator with end attribute
    print(10,20,30,sep=':',end='***')
    print(40,50,60,sep=':')
    print(70,80,90,sep='**',end='$$')
    print(100,200)
    # O/P:-