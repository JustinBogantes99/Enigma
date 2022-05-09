from enigma import Enigma

if __name__=='__main__':
    mensaje="Hola esto es un mensaje."
    maquina = Enigma()
    # Se configura la máquina
    maquina.config(stackerbrett={" ":" ",".":"."},keyword="ABC")
    x=maquina.cifrarPalabra(mensaje)
    print("'{}' es '{}'".format(mensaje,x))
    # Se vulve a configurar la máquina para decifrar
    maquina.config(stackerbrett={" ":" ",".":"."},keyword="ABC")
    y=maquina.cifrarPalabra(x)
    print("'{}' es '{}'".format(x,y))