f1 = open('C:/Users/arman.ansari_infobea/Downloads/MyImage.jpg', 'rb')
data = f1.read()

# f2 = open('MyImage_copy.jpg', 'wb')
f2 = open('MyImage_copy.png', 'wb')
f2.write(data)

print('Udemy guido image is ready')

# Closing the files
f1.close()
f2.close()
