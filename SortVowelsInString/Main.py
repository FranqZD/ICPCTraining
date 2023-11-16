#Link Problem:
#https://leetcode.com/problems/sort-vowels-in-a-string/?envType=daily-question&envId=2023-11-13
#Franq

s = "lEetcOde"
ListaNew = []
for l in s:
    if l =="A" or l=="E" or l=="I" or l=="O" or l=="U" or l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
        ListaNew.append(l)
ListaNew.sort()
ListaClin = []
n = 0
for l in s:
    if l =="A" or l=="E" or l=="I" or l=="O" or l=="U" or l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
        ListaClin.append(ListaNew[n])
        n+=1
    else:
        ListaClin.append(l)
s = ''.join(ListaClin)


    
    