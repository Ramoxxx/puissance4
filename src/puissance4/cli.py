from __future__ import annotations

import os

from .joueur import Joueur
from .partie import Partie


def main() -> None:
    print("Bienvenue au Puissance 4 !")
    print("Les colonnes vont de 1 a 7.")

    joueur1 = Joueur("Joueur 1", "🟡")
    joueur2 = Joueur("Joueur 2", "🔴")
    partie = Partie(joueur1, joueur2)

    while not partie.est_terminee():
        os.system('cls')
        print(f"\033[44m {partie} \033[0m")
        choix = input(f"{partie.joueur_actuel.nom} choisissez une colonne (1-7) : ")

        try:
            colonne = int(choix) - 1
            if not 0 <= colonne <= 6:
                raise ValueError
            if partie.jouer_coup(colonne):
                os.system('cls')
                print(f"\033[44m {partie} \033[0m")
                if partie.gagnant is not None:
                    print(f"Victoire de {partie.gagnant.nom} !")
                else:
                    print("Match nul !")
                break
        except ValueError:
            print("Veuillez entrer un nombre entre 1 et 7.")


if __name__ == "__main__":
    main()