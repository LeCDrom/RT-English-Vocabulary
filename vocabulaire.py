#Le programme doit:
#Proposer un mot en anglais, l'utilisateur doit pouvoir répondre, et le programme donne la réponse

print("--------------------------------------")
print('Commandes et informations avec: "help"')
print("--------------------------------------")

while True:

    import random

    vocabulaire = 'vocabulaire.txt'

    liste_ligne = []

    with open(vocabulaire , 'r', encoding='utf-8') as fichier:

        for ligne in fichier:

            liste_ligne.append(ligne)

        ligne_random = random.choice(liste_ligne)    

        sortie_anglais = ""
        question = ""

        for partie_anglais in ligne_random:

            if partie_anglais != ':':

                sortie_anglais = sortie_anglais + partie_anglais

            else:

                question = sortie_anglais

        sortie_française = ""
        sortie_française_retournée = ""
        ligne_random_retournee = ""
        réponse_retournée = ""
        réponse = ""

        for lettre in ligne_random:

            ligne_random_retournee = lettre + ligne_random_retournee

        for partie_française_retournée in ligne_random_retournee:

            if partie_française_retournée != ":":

                sortie_française_retournée = sortie_française_retournée + partie_française_retournée

            else:

                réponse_retournée = sortie_française_retournée

        for lettre in réponse_retournée:

            réponse = lettre + réponse
    
        print("Traduit ce mot en Français:")
        print("")
        print(question)
        print("")

        saisie = input()

        if saisie.lower()=="stop":
            break
        if saisie.lower()=="help":
            print("-----------------------------------------------------------------------")
            print('Pour arrêter, écrire "stop"')
            print('Pour passer la question, faire Entrer')
            print('Pour valider la question, faire Entrer')
            print("-----------------------------------------------------------------------")
            print("N'hésitez pas à modifier le fichier vocabulaire.txt si c'est nécessaire")            
            print("-----------------------------------------------------------------------")

        print("")
        print("La réponse est:", réponse)

        saisie = input()

        if saisie.lower()=="stop":
            break
        if saisie.lower()=="help":
            print("-----------------------------------------------------------------------")
            print('Pour arrêter, écrire "stop"')
            print('Pour passer la question, faire Entrer')
            print('Pour valider la question, faire Entrer')
            print("-----------------------------------------------------------------------")
            print("N'hésitez pas à modifier le fichier vocabulaire.txt si c'est nécessaire")            
            print("-----------------------------------------------------------------------")


    import random

    vocabulaire = 'vocabulaire.txt'

    liste_ligne = []

    with open(vocabulaire , 'r', encoding='utf-8') as fichier:

        for ligne in fichier:

            liste_ligne.append(ligne)

        ligne_random = random.choice(liste_ligne)    

        sortie_anglais = ""
        question = ""

        for partie_anglais in ligne_random:

            if partie_anglais != ':':

                sortie_anglais = sortie_anglais + partie_anglais

            else:

                question = sortie_anglais

        sortie_française = ""
        sortie_française_retournée = ""
        ligne_random_retournee = ""
        réponse_retournée = ""
        réponse = ""

        for lettre in ligne_random:

            ligne_random_retournee = lettre + ligne_random_retournee

        for partie_française_retournée in ligne_random_retournee:

            if partie_française_retournée != ":":

                sortie_française_retournée = sortie_française_retournée + partie_française_retournée

            else:

                réponse_retournée = sortie_française_retournée

        for lettre in réponse_retournée:

            réponse = lettre + réponse


        print("")
        print("Traduit ce mot en Anglais:")
        print("")
        print(réponse)
        print("")

        saisie = input()

        if saisie.lower()=="stop":
            break
        if saisie.lower()=="help":
            print("-----------------------------------------------------------------------")
            print('Pour arrêter, écrire "stop"')
            print('Pour passer la question, faire Entrer')
            print('Pour valider la question, faire Entrer')
            print("-----------------------------------------------------------------------")
            print("N'hésitez pas à modifier le fichier vocabulaire.txt si c'est nécessaire")            
            print("-----------------------------------------------------------------------")

        print("")
        print("La réponse est:", question)

        saisie = input()

        if saisie.lower()=="stop":
            break
        if saisie.lower()=="help":
            print("-----------------------------------------------------------------------")
            print('Pour arrêter, écrire "stop"')
            print('Pour passer la question, faire Entrer')
            print('Pour valider la question, faire Entrer')
            print("-----------------------------------------------------------------------")
            print("N'hésitez pas à modifier le fichier vocabulaire.txt si c'est nécessaire")            
            print("-----------------------------------------------------------------------")



