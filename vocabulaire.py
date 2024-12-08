import random


def separer_fr_eng(ligne: str):
    """
    Sépare le mot anglais et français d'une ligne et les retourne sous forme de tuples
    """    
    if ligne != "Mots de liaisons" and ligne != "" and ligne != " ":
        partie_eng = ""
        partie_fr = ""

        for i in range(len(ligne)):
            if ligne[i] == ":":
                partie_eng = ligne[:i-1].strip()
                partie_fr = ligne[i+2:].strip()
                return partie_eng, partie_fr

def load_vocab_list(file: str="vocabulaire.txt") -> list:
    """
    Ouvre la liste de vocabulaire et l'ajoute à une liste
    """
    data = []
    with open(file, 'r') as f:
        for ligne in f:
            data.append(ligne)
        f.close()
    return data

def score_moyen(reponses_correctes: int, reponses_totales: int) -> float:
    """
    Calcule le nouveau score en %
    """
    if reponses_totales == 0:
        return 0
    return round((reponses_correctes/reponses_totales)*100, 1)

def void_e_accents(texte: str) -> str:
    """
    Remplace les accents en é, è ou ê en e
    """
    res = ""
    for char in texte:
        if char == "é" or char == "è" or char == "ê":
            res += "e"
        else:
            res += "e"
    return res

def help() -> str:
    """
    Afficher les commandes
    """
    print("\n==================== Apprentissage Vocabulaire ====================")
    print('- Tapez les commandes suivantes après le chevron ">>>"')
    print('- "résultats" / "resultats" -> afficher le résumé du score')
    print('- "smart" / "no-smart" -> activer / désactiver le mode intelligent')
    print()
    print('"help" ou "?" pour afficher ces indications')
    print("==================== ------------------------- ====================\n")



global liste
liste = load_vocab_list()

def ligne_random() -> tuple:
    return separer_fr_eng(random.choice(liste))


reponses_correctes = 0
reponses_totales = 0
score = 0.0
saisie = ""
cmd = ""
hardmode = ""
smart = 0

help()

mode_lelievre = input("⚠️  Activer le mode Lelièvre ? ⚠️  (y|n): ")

if mode_lelievre == "y":
    hardmode = " 💀 "

while cmd != "exit":
    """
    Programme principal
    """

    ligne = ligne_random()
    english = ligne[0]
    francais = ligne[1]

    mode = random.choice((0, 1))

    if mode == 0:
        print(f'\n----------{hardmode}-----------\n\nTraduction de "{english}" en français :\n')
        saisie = input("Prompt : ")
        
        if mode_lelievre == "y":
            if void_e_accents(saisie.lower()) == void_e_accents(francais.lower()):
                print("✅ Correct !")
                reponses_correctes += 1
                reponses_totales += 1
            else:
                print(f'❌ Faux. La bonne réponse était "{francais}"')
                reponses_totales += 1

                if smart == 1:
                    for _ in range(10):
                        liste.append(f"{english} : {francais}")

            score = score_moyen(reponses_correctes, reponses_totales)
            cmd = input(f"\n...Score : {score}% >>> ")

            if cmd == "smart":
                smart = 1
                print("\n[Mode intelligent activé]")
            elif cmd == "no-smart":
                smart = 0
                print("\n[Mode intelligent désactivé]")
            elif cmd == "show-liste":
                print(liste)
            elif cmd == "show-len-liste":
                print(len(liste))
            elif cmd == "help" or cmd == "?":
                help()

            if (cmd == "résultats" or cmd == "resultats") and mode_lelievre == "y":
                print(f"\nRéponses correctes = {reponses_correctes}")
                print(f"Réponses totales = {reponses_totales}")

        else:
            print(f'\nCorrection : "{francais}"')
            cmd = input("\n>>> ")

            if cmd == "smart" or cmd == "no-smart":
                print("\n❌ Mode intelligent désactivé dans le mode simple ❌")
            if cmd == "résultats" or cmd == "resultats":
                print("\n❌ Score désactivé dans le mode simple ❌")
            elif cmd == "help" or cmd == "?":
                help()
        
    elif mode == 1:
        print(f'\n----------{hardmode}-----------\n\nTraduction de "{francais}" en anglais :\n')
        saisie = input("Prompt : ")
        
        if mode_lelievre == "y":
            if void_e_accents(saisie.lower()) == void_e_accents(english.lower()):
                print("✅ Correct !")
                reponses_correctes += 1
                reponses_totales += 1
            else:
                print(f'❌ Faux. La bonne réponse était "{english}"')
                reponses_totales += 1

                if smart == 1:
                    for _ in range(10):
                        liste.append(f"{english} : {francais}")

            score = score_moyen(reponses_correctes, reponses_totales)
            cmd = input(f"\n...Score : {score}% >>> ")

            if cmd == "smart":
                smart = 1
                print("\n[Mode intelligent activé]")
            elif cmd == "no-smart":
                smart = 0
                print("\n[Mode intelligent désactivé]")
            elif cmd == "show-liste":
                print(liste)
            elif cmd == "show-len-liste":
                print(len(liste))
            elif cmd == "help" or cmd == "?":
                help()

            if (cmd == "résultats" or cmd == "resultats") and mode_lelievre == "y":
                print(f"\nRéponses correctes = {reponses_correctes}")
                print(f"Réponses totales = {reponses_totales}")

        else:
            print(f'\nCorrection : "{english}"')
            cmd = input("\n>>> ")

            if cmd == "smart" or cmd == "no-smart":
                print("\n❌ Mode intelligent désactivé dans le mode simple ❌")
            if cmd == "résultats" or cmd == "resultats":
                print("\n❌ Score désactivé dans le mode simple ❌")
            elif cmd == "help" or cmd == "?":
                help()
