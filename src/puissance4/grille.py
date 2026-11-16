from __future__ import annotations


class Grille:
    """Represente la grille de jeu du Puissance 4."""

    LIGNES = 6
    COLONNES = 7
    VIDE = "⚫"

    def __init__(self) -> None:
        self.grille: list[list[str]] = [
            [self.VIDE for _ in range(self.COLONNES)]
            for _ in range(self.LIGNES)
        ]

    def jouer(self, colonne: int, symbole: str) -> int:
        """Place un jeton dans la colonne donnee et retourne la ligne occupee."""
        if not 0 <= colonne < self.COLONNES:
            raise ValueError(f"La colonne doit etre comprise entre 0 et {self.COLONNES - 1}.")

        if self.colonne_pleine(colonne):
            raise ValueError(f"La colonne {colonne + 1} est pleine.")

        for ligne in range(self.LIGNES - 1, -1, -1):
            if self.grille[ligne][colonne] == self.VIDE:
                self.grille[ligne][colonne] = symbole
                return ligne

        raise ValueError("Impossible de jouer dans cette colonne.")

    def colonne_pleine(self, colonne: int) -> bool:
        return self.grille[0][colonne] != self.VIDE

    def est_victoire(self, symbole: str) -> bool:
        for ligne in range(self.LIGNES):
            for colonne in range(self.COLONNES):
                if self.grille[ligne][colonne] != symbole:
                    continue

                if colonne <= self.COLONNES - 4 and all(
                    self.grille[ligne][colonne + offset] == symbole for offset in range(4)
                ):
                    return True

                if ligne <= self.LIGNES - 4 and all(
                    self.grille[ligne + offset][colonne] == symbole for offset in range(4)
                ):
                    return True

                if ligne <= self.LIGNES - 4 and colonne <= self.COLONNES - 4 and all(
                    self.grille[ligne + offset][colonne + offset] == symbole for offset in range(4)
                ):
                    return True

                if ligne <= self.LIGNES - 4 and colonne >= 3 and all(
                    self.grille[ligne + offset][colonne - offset] == symbole for offset in range(4)
                ):
                    return True

        return False

    def est_pleine(self) -> bool:
        return all(self.grille[0][colonne] != self.VIDE for colonne in range(self.COLONNES))

    def afficher(self) -> str:
        lignes: list[str] = []
        for ligne in self.grille:
            lignes.append(" ".join(cell for cell in ligne))
        separator = "-" * (self.COLONNES * 4 - 1)
        header = " ".join(str(colonne + 1) for colonne in range(self.COLONNES))
        return "\n".join([header, separator, *lignes])

    def __str__(self) -> str:
        return self.afficher()
