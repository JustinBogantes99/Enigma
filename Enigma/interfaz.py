# -*- coding: utf-8 -*-
from cgitb import text
from importlib.resources import path
from multiprocessing.connection import wait
from time import sleep
from tkinter import *
from unittest.mock import patch #Libreria para crear la interfaz grafica
from enigma import Enigma
teclado=[["Q","W","E","R","T","Y","U","I","O"],["P","A","S","D","F","G","H","J","K"],["L","Ñ","Z","X","C","V","B","N","M"]]
listaLabels=[]
listaBotones=[]
listarotor=[]
rotor=["","",""]   
palabra=""
maquina = Enigma()
maquina.config()
rotorIz=0
rotorCentro=0
rotorDer=0
contIz=0
contCentro=0
contDer=0

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#E:Recibe un boton y un color
#S:Le cambia el color al fondo del boton
#R:No tiene
def cambiar_color(boton,color,):
    boton.config(bg=color)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def cerrar_ventana_ayuda(abrir,cerrar):
    abrir.withdraw()
    cerrar.deiconify()

def cambiarLabel(letra,canvas):
    global rotorDer,rotorCentro,rotorIz,contDer,contCentro,rotor1,rotor2,rotor3,palabraEncriptada,palabraDesencriptada
    palabraDesencriptada['text']=palabraDesencriptada['text']+letra
    x=maquina.cifrar(letra)
    rotor1['text']=maquina.rotorI[0][0]
    rotor2['text']=maquina.rotorII[0][0]
    rotor3['text']=maquina.rotorIII[0][0]
    palabraEncriptada['text']=palabraEncriptada['text']+x    
    for valor in listaLabels:
        if valor['text']==x:
            valor.config(background="red")
            
            canvas.update()
            sleep(1)
            valor.config(background="#FFE4B5")
            canvas.update()
            break
    
def ventana_iniciar(ventana):
    global listaLabels,listaBotones,rotor1,rotor2,rotor3,palabraEncriptada,palabraDesencriptada
    frme_venta_iniciar=Frame(ventana,width=750,height=695,bg="green")
    frme_venta_iniciar.place(x=0,y=0)
    frm_secundario=Frame(ventana,width=400,height=200,bg="red")
    frm_secundario.place(x=20,y=400)
    rotor1=Label(ventana,text=maquina.rotorI[0][rotorDer],bd=30,bg="#FFE4B5")
    rotor1.place(x=210,y=250)
    rotor2=Label(ventana,text=maquina.rotorII[0][rotorCentro],bd=30,bg="#FFE4B5")
    rotor2.place(x=110,y=250)
    rotor3=Label(ventana,text=maquina.rotorIII[0][rotorIz],bd=30,bg="#FFE4B5")
    rotor3.place(x=10,y=250)
    palabraEncriptada=Label(ventana,text="Mensaje encriptado: ",bd=10,bg="#FFE4B5")
    palabraEncriptada.place(x=10,y=310)
    palabraDesencriptada=Label(ventana,text="Mensaje: ",bd=10,bg="#FFE4B5")
    palabraDesencriptada.place(x=10,y=340)
    btn_salir=Button(ventana,text="Reiniciar",command=lambda:[],bg="#FFE4B5",highlightthickness=0,bd=0,activebackground="khaki1")
    btn_salir.place(x=80,y=640)

    #rotor2=Label(frme_venta_iniciar,text=maquina.rotorII[1][0],bd=30,bg="#FFE4B5").place(x=400,y=400)
    #rotor2=Label(frme_venta_iniciar,text=maquina.rotorIII[1][0],bd=30,bg="#FFE4B5").place(x=400,y=400)
    for i in range(len(teclado)):
        for j in range(len(teclado[0])):
            casilla2=Canvas(frme_venta_iniciar,highlightthickness=0,bd=1,width=90,height=93) 
            casilla2.grid(row=i+10,column=j+10,padx=6)
            casilla=Canvas(frm_secundario,highlightthickness=0,bd=1,width=90,height=93,bg="blue") 
            casilla.grid(row=i,column=j)
            luces=Label(casilla2,text=teclado[i][j],bd=30,bg="#FFE4B5")
            listaLabels+=[luces]
            btn=Button(casilla,bg="white",text=teclado[i][j],width=10,height=3,command=lambda i=i,j=j:[cambiarLabel(teclado[i][j],casilla2)])
            listaBotones+=[btn] 
    crearBotonLaber() 

def crearBotonLaber():
    global listaLabels,listaBotones
    largo=len(listaBotones)
    fila=0
    columna=0
    for x in listaLabels:
        for y in listaBotones:
            y.grid(row=fila,column=columna)
        x.grid(row=fila,column=columna)
        fila+=1     
        columna+=1         

ventana_principal=Tk()  
ventana_principal.title("Enigma")     
ventana_principal.geometry("750x695+280+0")
ventana_principal.config(bg="#FFE4B5")
ventana_principal.resizable(0,0)
ventana_iniciar(ventana_principal)
ventana_principal.mainloop() 
