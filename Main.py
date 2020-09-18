1# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:55:59 2020

******@author: Anass  NASSIRI  IDSD ************

******this source code is created by Me*********
"""
import funanas

def Main():
    print(""" ====Election 2020==== """)
    print("Actuellement "+str(funanas.findvotan())+" personnes ont voté sur ("+str(funanas.countlistelectoral())+")")
    
    print("--------------------------------------------------")
    #funanas.reed_list1()
    print("""	1 : Inscription
	2 : Liste codes --> candidat
	3 : Voter
	4 : Statistiques
	5 : Quitter
--------------------------------------------------""")
    selection=input("Enter choice: ")
    if selection=="1":
        nom=input("Saisir votre nom :")
        nom=nom.upper()
        prenom=input("Saisir votre prenom :")
        prenom=prenom.upper()
        print("*** inscription réussie ***")
        print("Voici vos informations :")
        passwordd=funanas.password()
        code=funanas.logincount()
        code=str(code)
        funanas.liste_des_vote(code , prenom , nom , passwordd)
        print("logine: ",code+"  password",passwordd)
        Main()
    elif selection=="2":
        print("*** Liste des candidats ***")
        funanas.reed_list()
        Main()
    elif selection=="3":
        y="Y"
        d=False
        s=True
        code=input("Saisir votre code :")
        code=code.upper()
        passwordd=input("Saisir votre passwordd :")
        passwordd=passwordd.upper()
        with open("La_liste_électorales.txt","r") as file:
            for i in file:
                if passwordd in i:
                    if code in i:
                        d=True
                        break
                else:
                    continue
        if d==s:
               prenom=funanas.find_name(passwordd)
               print("***Bienvenue "+prenom+"***")
               funanas.marque_votan(passwordd)
               funanas.reed_list()
               e=input("Enter choice: ")
               e=e.upper()
               f=input("Confirmer votre choix (Y/N): ")
               f=f.upper()
               if f==y:
                   funanas.vote(e)
                   print("\n*******Operation succeful********")
                   
                   Main()
               else:
                   Main()
        else:
            print("*** code et/ou password incorrect ***")
            print("***vou etez sur d'etre inscrit a la liste electorall ??***")
            
            Main()
 
    elif selection=="4":
        print("*** Résultat de l'élection : ***")
        print("Nombre de votants : ",str(funanas.findvotan())+"/"+str(funanas.countlistelectoral())+'\n')
        funanas.statistique()
        Main()
    elif selection=="5":
        print("*********Thank you for your attention*********")
        exit
    else:
        print("\n"+"*******Invalid choice!!! Enter 1-5*******"+"\n")
        Main()
Main()
