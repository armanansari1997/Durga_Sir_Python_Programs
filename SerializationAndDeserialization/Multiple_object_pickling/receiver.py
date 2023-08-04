import pickle

f = open('serial2.abc', 'rb')
print('Deserializing/Unpickling employee object and printing data...')
while True:
    try:
        new_obj = pickle.load(f)  # to unpickle we used load(file) function
        new_obj.display()
    except EOFError:
        f.close()
        break
print('Deserialization/Unpickling of all employee objects are completed')

