#  multi_inherit.py

class Scanner:
    def scan():
        print('scan() method from the Scanner class.')

class Printer:
    def print():
        print('print() method from the Printer class.')

class Fax:
    def send():
        print('send() method from the Fax class.')

    def print():
        print('print() method from the Fax class.')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass