# Deserialization / Unpickling
import pickle
from emp import Employee

f = open('receiver.abc', 'rb')
while True:
    try:
        emp = pickle.load(f)
        emp.display()
    except EOFError:
        f.close()
        break

