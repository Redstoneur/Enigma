########################################################################################################################
########################################### Reflector ##################################################################
########################################################################################################################

class Reflector:
    """
    Class Reflector
    Classe qui permet de simuler le fonctionnement d'un reflector
    """
    wiring: str = None

    def __init__(self, wiring: str) -> None:
        """
        Constructeur de la classe Reflector
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
        Affiche le reflector
        """
        return f"Reflector: {self.wiring}"


if __name__ == "__main__":
    # test de la classe Reflector
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    print(reflector)
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(i, reflector.encrypt(i), reflector.decrypt(i))
