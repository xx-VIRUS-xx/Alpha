import Alphabets

alpha=Alphabets.Alpha_Dict
name=input()
for i in alpha[name[0]].pattern():
    print(i)
    
    