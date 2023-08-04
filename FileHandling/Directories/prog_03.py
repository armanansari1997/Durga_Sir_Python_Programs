# 'To Create a subdirectory in valmiki123'
import os

os.mkdir('valmiki123/varun123')
print('varun123 directory created inside valmiki123')


# Note :
# 1. If the specified directory is already exist then we will get FileExistError
# 2. Compulsory base directory should be available already, otherwise we will get 'FileNotFoundError'

# We can use mkdir function to create directory anywhere in our system. But we have to use absolute path
# Create a directory called PythonTestDirectory in the Desktop

os.mkdir('C:/Users/arman.ansari_infobea/Desktop/PythonTestDirectory')
print('Directory is created on the specified location')
