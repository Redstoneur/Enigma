########################################################################################################################
########################################### Plugboard ##################################################################
########################################################################################################################

class Plugboard:
    """
    Class Plugboard
    Classe qui permet de simuler le fonctionnement d'un plugboard
    """
    wiring: str = None

    def __init__(self, wiring: str) -> None:
        """
        Constructeur de la classe Plugboard
        """
        self.wiring: str = wiring

    def encrypt(self, letter: str) -> str:
        """
        Encrypte une lettre
        """
        letter = self.wiring[ord(letter) - ord("A")]
        return letter

    def decrypt(self, letter: str) -> str:
        """
        Décrypte une lettre
        """
        letter = chr(self.wiring.index(letter) + ord("A"))
        return letter

    def __str__(self) -> str:
        """
        Affiche le plugboard
        """
        return f"Plugboard: {self.wiring}"


if __name__ == "__main__":
    # test de la classe Plugboard
    plugboard = Plugboard("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(plugboard)
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(i, plugboard.encrypt(i), plugboard.decrypt(i))
