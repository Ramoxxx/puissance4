import unittest

from puissance4.grille import Grille


class TestGrille(unittest.TestCase):
    def test_ajout_jeton_dans_colonne(self):
        grille = Grille()
        row = grille.jouer(3, "X")

        self.assertEqual(row, 5)
        self.assertEqual(grille.grille[5][3], "X")

    def test_deux_jetons_s_ajoutent_sur_les_lignes(self):
        grille = Grille()

        grille.jouer(0, "X")
        grille.jouer(0, "O")

        self.assertEqual(grille.grille[5][0], "X")
        self.assertEqual(grille.grille[4][0], "O")

    def test_detection_victoire_horizontale(self):
        grille = Grille()

        for colonne in range(4):
            grille.jouer(colonne, "X")

        self.assertTrue(grille.est_victoire("X"))

    def test_colonne_pleine_renvoie_erreur(self):
        grille = Grille()

        for _ in range(6):
            grille.jouer(2, "X")

        with self.assertRaises(ValueError):
            grille.jouer(2, "O")


if __name__ == "__main__":
    unittest.main()
