# 'a'       open for writing, appending to the end of the file if it exists

with open('txt3', 'a') as f:
    f.write('\nJava')
    f.writelines('\nI just wanna switch my career into IT industry')
