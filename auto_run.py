import os
import time

contador=0

while True:
    contador+=1
    os.system("clear")
    print("Ejecutando el programa... Vez numero: " + str(contador))
    time.sleep(1)
    os.system("python3 auto_modify.py")

    if contador%100==0:
        os.system("rm auto_modify.py")
        os.system("touch auto_modify.py")
        program = open("auto_modify.py", "r+")
        backup = open("backup.txt", "r")
        for line in backup:
            program.write(line)
        backup.close()
        program.close()

    if contador%25==0:
        os.system("git gc --aggressive")
        os.system("git push")
