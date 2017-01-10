import os
import random

string = "aaaEEEiiiOOOuuu"
lista = [1,2,3,4,5,6,7,8,9]

python_instructions = [
"\nprint(string)",
"\nstring+='a'",
"\nstring+='b'",
"\nstring+='c'",
"\nstring+='d'",
"\nstring+='e'",
"\nstring+='f'",
"\nstring+='g'",
"\nlista = [1,2,3,4,5,6,7,8,9]",
"\nprint(lista)"
]

rand_int = random.randint(0,len(python_instructions)-1)
command_to_insert = python_instructions[rand_int]

program = open("auto_modify.py", "r+")
for line in program:
    if "#" in line:
        break

program.write(command_to_insert)
program.close()
os.system("./commit.sh " + "añadido")

print("---------- OUTPUT AUTO_MODIFY ----------")

##########################################################

print(string)
print(string)
string+='b'
string+='b'
string+='f'
print(lista)
string+='d'
string+='d'
print(string)
string+='f'
string+='a'
string+='f'
string+='b'
string+='a'
string+='c'
string+='f'
string+='g'
print(lista)
print(string)
string+='g'
string+='f'
lista = [1,2,3,4,5,6,7,8,9]
string+='b'
string+='d'
string+='e'
print(string)
string+='d'
string+='c'
string+='g'
print(string)
string+='g'
string+='c'
string+='a'
string+='g'
string+='f'
string+='b'
string+='a'
print(string)
string+='g'
string+='e'
string+='d'
string+='d'
string+='e'
string+='a'
string+='b'
string+='c'
string+='c'
string+='d'
string+='a'
string+='d'