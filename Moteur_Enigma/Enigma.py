import typing as ty

from Moteur_Enigma import Rotor, Reflector, Plugboard


########################################################################################################################
########################################### Enigma #####################################################################
########################################################################################################################


class Enigma:
    """
    Class Enigma
    Classe qui permet de simuler le fonctionnement de l'Enigma
    """
    rotors: ty.List[Rotor] = []
    reflector: Reflector = None
    plugboard: Plugboard = None

    def __init__(self, rotors: ty.List[Rotor], reflector: Reflector, plugboard: Plugboard) -> None:
        """
        Constructeur de la classe Enigma
        :param rotors: Liste des rotors
        :param reflector: Reflector
        :param plugboard: Plugboard
        """
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def add_rotor(self, rotor: Rotor) -> None:
        """
        Ajoute un rotor à l'Enigma
        :param rotor: Rotor
        """
        self.rotors.append(rotor)

    def set_reflector(self, reflector: Reflector) -> None:
        """
        Définit le reflector de l'Enigma
        :param reflector: Reflector
        """
        self.reflector = reflector

    def set_plugboard(self, plugboard: Plugboard) -> None:
        """
        Définit le plugboard de l'Enigma
        :param plugboard: Plugboard
        """
        self.plugboard = plugboard

    def encrypt(self, letter: str) -> str:
        """
        Encrypte une lettre
        """
        letter = self.plugboard.encrypt(letter)
        for rotor in self.rotors:
            letter = rotor.encrypt(letter)
        letter = self.reflector.encrypt(letter)
        for rotor in reversed(self.rotors):
            letter = rotor.decrypt(letter)
        letter = self.plugboard.encrypt(letter)
        return letter

    def decrypt(self, letter: str) -> str:
        """
        Décrypte une lettre
        """
        letter = self.plugboard.decrypt(letter)
        for rotor in reversed(self.rotors):
            letter = rotor.decrypt(letter)
        letter = self.reflector.decrypt(letter)
        for rotor in self.rotors:
            letter = rotor.encrypt(letter)
        letter = self.plugboard.decrypt(letter)
        return letter

    def encrypt_message(self, message: str) -> str:
        """
        Encrypte un message
        """
        encrypted_message = ""
        for letter in message:
            encrypted_message += self.encrypt(letter)
        return encrypted_message

    def decrypt_message(self, message: str) -> str:
        """
        Décrypte un message
        """
        decrypted_message = ""
        for letter in message:
            decrypted_message += self.decrypt(letter)
        return decrypted_message

    def __str__(self) -> str:
        """
        Affiche l'Enigma
        """
        str: str = "Enigma :\n"
        for rotor in self.rotors:
            str += " -  " + rotor.__str__() + "\n"
        str += "\n" + \
               " -  " + self.reflector.__str__() + "\n" + \
               " -  " + self.plugboard.__str__()
        return str


if __name__ == "__main__":
    # test de la classe Enigma
    rotors: ty.List[Rotor] = [Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"), Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
                              Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")]
    reflector: Reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard: Plugboard = Plugboard("AV BS CG DL FU HZ IN KM OW RX EJ PT QY")

    enigma: Enigma = Enigma(rotors, reflector, plugboard)
    print(enigma)
    message = "HELLOWORLD"
    encrypted_message = enigma.encrypt_message(message)
    decrypted_message = enigma.decrypt_message(encrypted_message)
    print()
    print(f"Message: '{message}'")
    print(f"Message encrypté: '{encrypted_message}'")
    print(f"Message décrypté: '{decrypted_message}'")
