########################################################################################################################
########################################### Rotor ######################################################################
########################################################################################################################

class Rotor:
    """
    Class Rotor
    Classe qui permet de simuler le fonctionnement d'un rotor
    """
    wiring: str = None
    turnover: str = None
    position: int = 0

    def __init__(self, wiring: str, turnover: str) -> None:
        """
        Constructeur de la classe Rotor
        """
        self.wiring: str = wiring
        self.turnover: str = turnover

    def encrypt(self, letter: str) -> str:
        """
        Encrypte une lettre
        """
        letter = chr((ord(letter) - ord("A") + self.position) % 26 + ord("A"))
        letter = self.wiring[ord(letter) - ord("A")]
        letter = chr((ord(letter) - ord("A") - self.position) % 26 + ord("A"))
        self.position = (self.position + 1) % 26
        return letter

    def decrypt(self, letter: str) -> str:
        """
        Décrypte une lettre
        """
        letter = chr((ord(letter) - ord("A") + self.position) % 26 + ord("A"))
        letter = chr(self.wiring.index(letter) + ord("A"))
        letter = chr((ord(letter) - ord("A") - self.position) % 26 + ord("A"))
        self.position = (self.position + 1) % 26
        return letter

    def __str__(self) -> str:
        """
        Affiche le rotor
        """
        return f"Rotor: {self.wiring} {self.turnover} {self.position}"


if __name__ == "__main__":
    # Test de la classe Rotor
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    print(rotor)
    letter = "A"
    letter_encrypted = rotor.encrypt(letter)
    letter_decrypted = rotor.decrypt(letter_encrypted)
    print(letter, letter_encrypted, letter_decrypted)


