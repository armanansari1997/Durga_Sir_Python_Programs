num1 = 10
num2 = 20
num3 = 30
if num1 < num2:
    raise Exception('Number1 is less Number2')
elif num2 < num3:
    raise Exception('Number2 is less than Number3')
else:
    print('There is no Exception')
