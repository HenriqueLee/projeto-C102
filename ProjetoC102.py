import os
import shutil


fromdir="E:/Downloads/"
todir= "C:/Users/Mauro/Desktop/Arquivos\ documentos/"
listadearquivos= os.listdir(fromdir)
print(listadearquivos)

for filename in listadearquivos:
    name, extensions= os.path.splitext(filename)
    if extensions==" ":
        continue
    if extensions in [".txt" ".doc", ".docx", ".pdf"]:
        path1= fromdir+filename
        path2= todir
        path3= todir+filename
        if os.path.exists(path2):
            print("movendo o arquivo", filename)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
