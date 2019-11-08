import os

#print(os.getcwd())
#print(os.listdir())

for root, dirs, files, in os.walk(os.getcwd()):
    print("Root: " + str(root))
    print("Diretórios: " + str(dirs))
    print("Arquivos: " + str(files))