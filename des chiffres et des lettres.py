import os
ka = "abcdefg"
lettr = []
for i in ka:
    lettr.append(i)

g = open("C:/Users/emmanuel cardot/Desktop/python vrmt cools/listes mots français sans accents.txt",'r')

def jeu(list,st):
    if len(st)>len(list):
        return False

    for i in range(len(st)):
        if st[i]!= ' ':
            if st.count(st[i])>list.count(st[i]):
                return False
    return True
taille = 0
grosmot = ""
k = 0
for mot in g:
    mot = mot[0:-1]

    if jeu(lettr,mot) == True:
        if len(mot)==k:
            listemot.append(mot)
        elif len(mot)>k:
            listemot = []
            listemot.append(mot)
            k = len(mot)


print(listemot)