from code import interact
from distutils.command.config import config
from string import ascii_lowercase, ascii_uppercase
from textwrap import indent


class Enigma:
    def __init__(self) -> None:
        self.alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.stackerbrett=None
        self.reflector="YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.rotorI=["ABCDEFGHIJKLMNOPQRSTUVWXYZ","BDFHJLCPRTXVZNYEIWGAKMUSQO"]
        self.rotorII=["ABCDEFGHIJKLMNOPQRSTUVWXYZ","AJDKSIRUXBLHWTMCQGZNPYFVOE"]
        self.rotorIII=["ABCDEFGHIJKLMNOPQRSTUVWXYZ","EKMFLGDQVZNTOWYHXUSPAIBRCJ"]

    def config(self,stackerbrett={" ":" "},keyword="AAA"):
        self.stackerbrett=stackerbrett
        self.configRotor("rotorI",keyword[0])
        self.configRotor("rotorII",keyword[1])
        self.configRotor("rotorIII",keyword[2])

    def cifrar(self,letra:str):
        if letra not in self.stackerbrett:
            if letra in self.alfabeto:
                letraCifrada=""
                pos=self.alfabeto.index(letra)
                #RotorI
                letraCifrada=self.rotorI[1][pos]
                pos=self.rotorI[0].index(letraCifrada)
                #RotorII
                letraCifrada=self.rotorII[1][pos]
                pos=self.rotorII[0].index(letraCifrada)
                #RotorIII
                letraCifrada=self.rotorIII[1][pos]
                pos=self.rotorIII[0].index(letraCifrada)
                #Reflector
                letraCifrada=self.reflector[pos]
                pos=self.alfabeto.index(letraCifrada)
                #RotorIII
                letraCifrada=self.rotorIII[0][pos]
                pos=self.rotorIII[1].index(letraCifrada)
                #RotorII
                letraCifrada=self.rotorII[0][pos]
                pos=self.rotorII[1].index(letraCifrada)
                #RotorI
                letraCifrada=self.rotorI[0][pos]
                pos=self.rotorI[1].index(letraCifrada)

                self.step()
                return self.alfabeto[pos]
            else:
                #No reconoce el caracter
                return "*"
        else:
            return self.stackerbrett[letra]
    
    def step(self):
        self.rotar("rotorI")
        if self.rotorI[0][0]==self.alfabeto[0]:
            self.rotar("rotorII")
            if self.rotorII[0][0]==self.alfabeto[0]:
                self.rotar("rotorIII")

    def rotar(self,nombreRotor):
        rotor=getattr(self,nombreRotor)
        externo=rotor[0][1:]+rotor[0][:1]
        interno=rotor[1][1:]+rotor[1][:1]
        rotor=[externo,interno]
        setattr(self,nombreRotor,rotor)


    def cifrarPalabra(self,palabra:str):
        palabra=palabra.upper()
        palabraCifrada=""
        for letra in palabra:
            palabraCifrada=palabraCifrada+self.cifrar(letra)
        return palabraCifrada

    def configRotor(self,nombreRotor:str,key:str):
        rotor=getattr(self,nombreRotor)
        index=rotor[0].index(key)
        externo=rotor[0][index:]+rotor[0][:index]
        interno=rotor[1][index:]+rotor[1][:index]
        rotor=[externo,interno]
        setattr(self,nombreRotor,rotor)
