# eg-1
try:
    print('try')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
print('---------------------------------')

# eg-2
try:
    print('try')
    print(10/0)
except Exception:
    print('except')
else:
    print('else')
finally:
    print('finally')
