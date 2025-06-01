import random


def separer_fr_eng(ligne: str) -> tuple:
    """
    Sépare le mot anglais et français d'une ligne et les retourne sous forme de tuple
    """    
    if ":" in ligne:
        partie_eng = ""
        partie_fr = ""

        for i in range(len(ligne)):
            if ligne[i] == ":":
                partie_eng = ligne[:i-1]
                partie_fr = ligne[i+2:]
                return partie_eng, partie_fr

def load_vocab_list(file: str="vocabulaire_s2.txt") -> list[tuple[str, str]]:
    """
    Ouvre la liste de vocabulaire et l'ajoute à une liste
    """
    vocab = []

    with open(file, 'r') as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne and ":" in ligne:
                anglais, francais = separer_fr_eng(ligne)
                if anglais and francais:
                    vocab.append((anglais, francais))
        f.close()
    return vocab

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

def clean(s):
    return void_e_accents(s.lower().strip())

def help() -> str:
    """
    Afficher les commandes
    """
    print("\n==================== Apprentissage Vocabulaire ====================")
    print('Tapez les commandes suivantes après le chevron ">>>"')
    print('- "résultats" -> afficher le résumé du score')
    print('- "smart"     -> activer le mode intelligent')
    print('- "no-smart"  -> désactiver le mode intelligent')
    print()
    print('"help" ou "?" pour afficher ces indications')
    print("===================================================================\n")



global liste
liste = load_vocab_list()

def ligne_random() -> tuple[str, str]:
    return random.choice(liste)


reponses_correctes = 0
reponses_totales = 0
score = 0.0
saisie = ""
cmd = ""
hardmode = ""
smart = 0

help()

mode_lelievre = input("⚠️  Activer le mode Lelièvre ? (y|n): ")

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

    if mode == 0:    # Anglais vers Français
        print(f'\n----------{hardmode}-----------\n\nTraduction de "{english}" en français :\n')
        saisie = input("Prompt : ")

        traductions_possibles = [fr for en, fr in liste if en == english]
        
        if mode_lelievre == "y":
            if clean(saisie) in [clean(trad) for trad in traductions_possibles]:
                print(f"✅ Correct ! Réponses acceptées : {', '.join(set(traductions_possibles))}")
                reponses_correctes += 1
                reponses_totales += 1
            else:
                print(f"❌ Faux. Réponses acceptées : {", ".join(set(traductions_possibles))}")
                reponses_totales += 1

                if smart == 1:
                    for _ in range(10):
                        liste.append((english, francais))

            score = score_moyen(reponses_correctes, reponses_totales)
            cmd = input(f"\n...Score : {score}% >>> ")

            if cmd == "smart":
                smart = 1
                print("\n[Mode intelligent activé]")
            elif cmd == "no-smart":
                smart = 0
                print("\n[Mode intelligent désactivé]")

            if (cmd == "résultats" or cmd == "resultats") and mode_lelievre == "y":
                print(f"\nRéponses correctes = {reponses_correctes}")
                print(f"Réponses totales = {reponses_totales}")

        else:
            print(f'\nRéponses acceptées : {", ".join(set(traductions_possibles))}')
            cmd = input("\n>>> ")

            if cmd == "smart" or cmd == "no-smart":
                print("\n❌ Mode intelligent désactivé dans le mode simple")
            if cmd == "résultats" or cmd == "resultats":
                print("\n❌ Score désactivé dans le mode simple")
        
        if cmd == "show-liste":
            print(liste)
        elif cmd == "show-len-liste":
            print(len(liste))
        elif cmd == "help" or cmd == "?":
            help()
        
    elif mode == 1:    # Français vers Anglais
        print(f'\n----------{hardmode}-----------\n\nTraduction de "{francais}" en anglais :\n')
        saisie = input("Prompt : ")

        traductions_possibles = [en for en, fr in liste if fr == francais]
        
        if mode_lelievre == "y":
            if clean(saisie) in [clean(trad) for trad in traductions_possibles]:
                print(f"✅ Correct ! Réponses acceptées : {", ".join(set(traductions_possibles))}")
                reponses_correctes += 1
                reponses_totales += 1
            else:
                print(f'❌ Faux. Réponses acceptées : {", ".join(set(traductions_possibles))}')
                reponses_totales += 1

                if smart == 1:
                    for _ in range(10):
                        liste.append((english, francais))

            score = score_moyen(reponses_correctes, reponses_totales)
            cmd = input(f"\n...Score : {score}% >>> ")

            if cmd == "smart":
                smart = 1
                print("\n[Mode intelligent activé]")
            elif cmd == "no-smart":
                smart = 0
                print("\n[Mode intelligent désactivé]")

            if (cmd == "résultats" or cmd == "resultats"):
                print(f"\nRéponses correctes = {reponses_correctes}")
                print(f"Réponses totales = {reponses_totales}")

        else:
            print(f'\nRéponses acceptées : {", ".join(set(traductions_possibles))}')
            cmd = input("\n>>> ")

            if cmd == "smart" or cmd == "no-smart":
                print("\n❌ Mode intelligent désactivé dans le mode simple")
            if cmd == "résultats" or cmd == "resultats":
                print("\n❌ Score désactivé dans le mode simple")
        
        if cmd == "show-liste":
            print(liste)
        elif cmd == "show-len-liste":
            print(len(liste))
        elif cmd == "help" or cmd == "?":
            help()
