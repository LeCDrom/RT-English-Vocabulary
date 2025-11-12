import random


def separer_fr_eng(ligne: str) -> tuple:
    """
    Sépare le mot anglais et français d'une ligne et les retourne sous forme de tuple.
    """    
    if ":" in ligne:
        partie_eng = ""
        partie_fr = ""

        for i in range(len(ligne)):
            if ligne[i] == ":":
                partie_eng = ligne[:i-1]
                partie_fr = ligne[i+2:]
                return partie_eng, partie_fr

def load_vocab_list(file: str="vocabulaire_s3.txt") -> list[tuple[str, str]]:
    """
    Ouvre la liste de vocabulaire et l'ajoute à une liste.
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

def void_accents(texte: str) -> str:
    res = ""
    for char in texte:
        if char in "éèê":
            res += "e"
        elif char in "ô":
            res += "o"
        elif char in "-'":
            res += " "
        elif char in ",":
            res += ""
        else:
            res += char
    return res


def clean(s):
    return void_accents(s.lower().strip())

def handle_command(commande, mode_apprentissage, reponses_correctes, reponses_totales):
    """
    Traitement des commandes entrées.
    """
    commande = commande.strip()
    if mode_apprentissage == 2:
        if commande == "!smart":
            smart = 1
            print("\n[Mode intelligent activé]")
        if commande == "!help" or commande == "!?":
            help()
        elif commande == "!no-smart":
            smart = 0
            print("\n[Mode intelligent désactivé]")
        elif commande == "!resultats":
            print(f"\nRéponses correctes = {reponses_correctes}")
            print(f"Réponses totales = {reponses_totales}")
        elif commande == "!exit":
            pass
        else:
            print(f'Commande inconnue : "{commande}"')
    else:
        if commande == "!smart" or commande == "!no-smart":
            print("\n❌ Mode intelligent désactivé dans le mode Normal et Rush")
        if commande == "!help" or commande == "!?":
            help()
        elif commande == "!resultats":
            print("\n❌ Score désactivé dans le mode Normal et Rush")
        elif commande == "!exit":
            pass
        else:
            print(f'Commande inconnue : "{commande}"')

    
def help() -> str:
    """
    Afficher les commandes
    """
    print("\n==================== Apprentissage Vocabulaire ====================")
    print('- "!smart"     -> activer le mode intelligent')
    print('- "!no-smart"  -> désactiver le mode intelligent')
    print('- "!exit"      -> quitter le programme')
    print()
    print('"!help" ou "!?" pour afficher ces indications')
    print("===================================================================\n")


global liste
liste = load_vocab_list()

def ligne_random() -> tuple[str, str]:
    """
    Retourne une ligne aléatoire, avec une priorité aux erreurs précédentes si le mode smart est activé.
    """
    return random.choice(liste)


reponses_correctes = 0
reponses_totales = 0
score = 0.0
saisie = ""
emoji = ""

global smart
smart = 0

help()

mode_apprentissage = int(input("1: Mode Normal\n2: Mode Lelièvre\n3: Mode Rush\n\nChoix mode : "))

if mode_apprentissage == 2:
    emoji = "[ 🐇 ]"
elif mode_apprentissage == 3:
    emoji = "[ 💀 ]"

while saisie != "!exit":
    """
    Programme principal
    """
    mode = random.choice((0, 1))

    if mode_apprentissage in [1, 2]:

        ligne = ligne_random()
        english = ligne[0]
        francais = ligne[1]

        if mode == 0:    # Anglais vers Français
            print(f'\n----------{emoji}-----------\n\nTraduction de "{english}" en français :\n')
            saisie = input("Prompt : ")

            if "!" in saisie:
                handle_command(saisie, mode_apprentissage, reponses_correctes, reponses_totales)
            else:

                traductions_possibles = [fr for en, fr in liste if en == english]
                
                if mode_apprentissage == 2:
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
            print(f'\n----------{emoji}-----------\n\nTraduction de "{francais}" en anglais :\n')
            saisie = input("Prompt : ")

            if "!" in saisie:
                handle_command(saisie, mode_apprentissage, reponses_correctes, reponses_totales)
            else:

                traductions_possibles = [en for en, fr in liste if fr == francais]
                
                if mode_apprentissage == 2:
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
    
    if mode_apprentissage == 3:
        # Parcourt la liste entière dans l'ordre et recommence quand une erreur est commise.

        print("Bienvenue dans le mode Rush. Une erreur et tout recommence.\nBonne chance...")

        reponses_correctes = 0
        i = 0

        while i != len(liste):
            ligne = liste[i]
            english = ligne[0]
            francais = ligne[1]
            mode = random.choice((0, 1))

            emoji = f"[ {reponses_correctes}/{len(liste)} ]"

            if mode == 0:    # Anglais vers Français
                print(f'\n----------{emoji}-----------\n\nTraduction de "{english}" en français :\n')
                saisie = input("Prompt : ")

                if "!" in saisie:
                    handle_command(saisie, mode_apprentissage, reponses_correctes, reponses_totales)
                else:

                    traductions_possibles = [fr for en, fr in liste if en == english]
                    
                    if clean(saisie) in [clean(trad) for trad in traductions_possibles]:
                        print(f"✅ Correct ! Réponses acceptées : {', '.join(set(traductions_possibles))}")
                        reponses_correctes += 1
                        i += 1
                    else:
                        print(f"❌ Faux. Réponses acceptées : {", ".join(set(traductions_possibles))}")
                        print(f"Vous avez échoué avec une série de {reponses_correctes}...")
                        i = 0
            
            elif mode == 1:    # Français vers Anglais
                print(f'\n----------{emoji}-----------\n\nTraduction de "{francais}" en anglais :\n')
                saisie = input("Prompt : ")

                if "!" in saisie:
                    handle_command(saisie, mode_apprentissage, reponses_correctes, reponses_totales)
                else:

                    traductions_possibles = [en for en, fr in liste if fr == francais]
                    
                    if clean(saisie) in [clean(trad) for trad in traductions_possibles]:
                        print(f"✅ Correct ! Réponses acceptées : {", ".join(set(traductions_possibles))}")
                        reponses_correctes += 1
                        i += 1
                    else:
                        print(f'❌ Faux. Réponses acceptées : {", ".join(set(traductions_possibles))}')
                        print(f"Vous avez échoué avec une série de {reponses_correctes}...")
                        i = 0

        print("Bravo vous connaissez votre vocabulaire ! Bon examen.")


print("\nArrêt...")
