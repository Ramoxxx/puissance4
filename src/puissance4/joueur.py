from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Joueur:
    nom: str
    symbole: str

    def __post_init__(self) -> None:
        if len(self.symbole) != 1:
            raise ValueError("Le symbole d'un joueur doit contenir exactement un caractere.")
        if self.symbole == " ":
            raise ValueError("Le symbole d'un joueur ne peut pas etre un espace.")
