# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:45:11 2020

******@author: Anass  NASSIRI  IDSD ************

******this source code is created by Me*********
"""

#pour crie lobjet lapremiere fois
def vote_cree(a):
    import  pickle
    
    votes={"C1":[],"C2":[],"C3":[],"C4":[]}
    with open('résultat_des_votes', 'ab') as file:
        mon_pickler = pickle.Pickler(file)
        mon_pickler.dump(votes)
#pour vote
def vote(a):
    import pickle
    a1="C1"
    a2="C2"
    a3="C3"
    a4="C4"
    with open('résultat_des_votes', 'rb') as file:
        mon_dipickler=pickle.Unpickler(file)
        votes=mon_dipickler.load()
    if a1 == a:
       votes["C1"].append(1)
    elif a2 == a:
        votes["C2"].append(1)
    elif a3 == a:
        votes["C3"].append(1)
    elif a4 == a:
        votes["C4"].append(1)
    with open('résultat_des_votes', 'wb') as file:
        mon_pickler = pickle.Pickler(file)
        mon_pickler.dump(votes)
        
#pour Enregistré les gens      
def liste_des_vote(code , prenom , nom , password):
    with open("La_liste_électorales.txt","a") as file:
        file.write('\n'+code+';'+prenom+';'+nom+';'+password)
        
  

#pour calculer le gens Enregistré
def countlistelectoral():
    with open("La_liste_électorales.txt","r") as file:
        L=file.readlines()
        n=len(L)-1
        return n
        
#pour genere password automatiquement    
def password():
    import random
    pwc=""
    pwn=""
    characters="ABCDEFGHIJKLMNOPQRSTVWXYZ"
    numbers="0123456789"
    for i in range(4):
        pwc=pwc+random.choice(characters)
        pwn=pwn+random.choice(numbers)
    p=pwc+"@"+pwn
    return p
#pour lecture list condidat
def reed_list():
    with open("list_condidat.txt", "r") as f :
        for ligne in f:
            print(ligne)    
#for read l'objet    
def readdict():
    import pickle
    with open('résultat_des_votes', 'rb') as file:
         mon_depickler = pickle.Unpickler(file)
         score_recupere = mon_depickler.load()
         print(score_recupere)
#pour affice menu
def reed_list1():
    with open("list_menu.txt", "r") as f :
        for ligne in f:
            print(ligne)
          
#pour login
def logincount():
    l=countlistelectoral()
    login=""
    while l<1000:
        if l<=9:
            login="E00"+str(l)
            return login
            break
        elif l<=99 and l>=10:
            login="E0"+str(l)
            return login
            break
        else:
            login="E"+str(l)
            return login
            break
#pour affiche les statistique        
def statistique():
    import pickle

    with open('résultat_des_votes', 'rb') as file:
         mon_depickler = pickle.Unpickler(file)
         score_recupere = mon_depickler.load()
         l=str(len(score_recupere["C1"]))
         a=str((sum(score_recupere["C1"])/findvotan()*100))
         print("YAHYA KHARBANE -->",l+" votes"+"("+a+ " %"+")" )
         l=str(len(score_recupere["C2"]))
         a=str((sum(score_recupere["C2"])/findvotan()*100))
         print("MOHCINE OUCHEN -->",l+" votes"+"("+a+ " %"+")" )
         l=str(len(score_recupere["C3"]))
         a=str((sum(score_recupere["C3"])/findvotan()*100))
         print("FATIMA EL JAMILI -->",l+" votes"+"("+a+ " %"+")" )
         l=str(len(score_recupere["C4"]))
         a=str((sum(score_recupere["C4"])/findvotan()*100))
         print("blanc -->",l+" votes"+"("+a+ " %"+")" )
    
#for find votan
def findvotan():
    v="v"
    count=0
    with open("La_liste_électorales.txt","r") as file:
        for i in file:
            if v in i:
                count+=1
        return count
#pour marque les gens qui vote       
def marque_votan(passwordd):
    with open('La_liste_électorales.txt', 'r+') as file:
        for i in file :
            if passwordd in i:
                a=i.split(';')
                a.append("v")
                a=a[4]
                a = ";".join(a)
                file.write(";"+a)
def find_name(passwordd):
    with open('La_liste_électorales.txt', 'r') as file:
        for i in file :
            if passwordd in i:
                a=i.split(';')
                a=a[1]
    return a