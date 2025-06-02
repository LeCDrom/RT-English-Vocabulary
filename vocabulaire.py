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

def handle_command(commande, smart, mode_lelievre, reponses_correctes, reponses_totales):
    """
    Traitement des commandes entrées
    """
    commande = commande.strip()
    if mode_lelievre == "y":
        if commande == "!smart":
            smart = 1
            print("\n[Mode intelligent activé]")
        elif commande == "!no-smart":
            smart = 0
            print("\n[Mode intelligent désactivé]")
        elif commande == "!resultats":
            print(f"\nRéponses correctes = {reponses_correctes}")
            print(f"Réponses totales = {reponses_totales}")
    else:
        if commande == "!smart" or commande == "!no-smart":
            print("\n❌ Mode intelligent désactivé dans le mode simple")
        elif commande == "!resultats":
            print("\n❌ Score désactivé dans le mode simple")

    if commande == "!help" or commande == "!?":
        help()

    # debug
    elif commande == "!show-liste":
        print(liste)
    elif commande == "!show-len-liste":
        print(len(liste))
    
def help() -> str:
    """
    Afficher les commandes
    """
    print("\n==================== Apprentissage Vocabulaire ====================")
    print('- "!smart"     -> activer le mode intelligent')
    print('- "!no-smart"  -> désactiver le mode intelligent')
    print('- "!exit"     -> quitter le programme')
    print()
    print('"!help" ou "!?" pour afficher ces indications')
    print("===================================================================\n")


global liste
liste = load_vocab_list()

def ligne_random() -> tuple[str, str]:
    return random.choice(liste)


reponses_correctes = 0
reponses_totales = 0
score = 0.0
saisie = ""
hardmode = ""
smart = 0

help()

mode_lelievre = input("⚠️  Activer le mode Lelièvre ? (y|n): ")

if mode_lelievre == "y":
    hardmode = "[ 💀 ]"

while saisie != "!exit":
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

        if ":" in saisie:
            handle_command(saisie, smart, mode_lelievre, reponses_correctes, reponses_totales)
        else:

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
                print(f"\n...Score : {score}% ({reponses_correctes}/{reponses_totales})")

            else:
                print(f'\nRéponses acceptées : {", ".join(set(traductions_possibles))}')
        
    elif mode == 1:    # Français vers Anglais
        print(f'\n----------{hardmode}-----------\n\nTraduction de "{francais}" en anglais :\n')
        saisie = input("Prompt : ")

        if ":" in saisie:
            handle_command(saisie, smart, mode_lelievre, reponses_correctes, reponses_totales)
        else:

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
                print(f"\n...Score : {score}% ({reponses_correctes}/{reponses_totales})")

            else:
                print(f'\nRéponses acceptées : {", ".join(set(traductions_possibles))}')

print("\nArrêt...")
