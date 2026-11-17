from __future__ import annotations

from .grille import Grille
from .joueur import Joueur


class Partie:
    def __init__(self, joueur1: Joueur, joueur2: Joueur) -> None:
        self.grille = Grille()
        self.joueurs = [joueur1, joueur2]
        self.joueur_actuel_index = 0
        self.gagnant: Joueur | None = None
        self.est_nulle = False

    @property
    def joueur_actuel(self) -> Joueur:
        return self.joueurs[self.joueur_actuel_index]

    def jouer_coup(self, colonne: int) -> bool:
        """Joue un coup et retourne True si la partie est terminee."""
        self.grille.jouer(colonne, self.joueur_actuel.symbole)

        if self.grille.est_victoire(self.joueur_actuel.symbole):
            self.gagnant = self.joueur_actuel
            return True

        if self.grille.est_pleine():
            self.est_nulle = True
            return True

        self.joueur_actuel_index = (self.joueur_actuel_index + 1) % len(self.joueurs)
        return False

    def est_terminee(self) -> bool:
        return self.gagnant is not None or self.est_nulle

    def __str__(self) -> str:
        return str(self.grille)
