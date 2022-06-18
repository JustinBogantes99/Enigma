# -*- coding: utf-8 -*-
from os import path as path2
from cgitb import text
from glob import glob
from importlib.resources import path
from multiprocessing.connection import wait
from time import sleep
from tkinter import *
from tkinter import ttk
from unittest.mock import patch #Libreria para crear la interfaz grafica
from enigma import Enigma
from tkinter import messagebox
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
mEncriptado=""

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
    global rotorDer,rotorCentro,rotorIz,contDer,contCentro,rotor1,rotor2,rotor3,palabraEncriptada,palabraDesencriptada,mEncriptado
    palabraDesencriptada['text']=palabraDesencriptada['text']+letra
    x=maquina.cifrar(letra)
    rotor1['text']=maquina.rotorI[0][0]
    rotor2['text']=maquina.rotorII[0][0]
    rotor3['text']=maquina.rotorIII[0][0]
    palabraEncriptada['text']=palabraEncriptada['text']+x
    mEncriptado=mEncriptado+x    
    for valor in listaLabels:
        if valor['text']==x:
            valor.config(background="red")
            
            canvas.update()
            sleep(1)
            valor.config(background="#FFE4B5")
            canvas.update()
            break
def cambiarKeyword(palabra):
    global rotor1,rotor2,rotor3
    if '' in palabra:
        messagebox.showerror(title="Error 404", message="Error si desea cambiar la keyword debe seleccionar los 3 valores")
    else:
        keyword=''
        for x in palabra:
            keyword+=x
        maquina.config(stackerbrett={" ":" ",".":"."},keyword=keyword)
        rotor1['text']=keyword[0]
        rotor2['text']=keyword[1]
        rotor3['text']=keyword[2]

def reiniciar():
    global rotor1,rotor2,rotor3,palabraEncriptada,palabraDesencriptada
    rotor1['text']='A'
    rotor2['text']='A'
    rotor3['text']='A'
    palabraDesencriptada['text']="Mensaje: "
    palabraEncriptada['text']="Mensaje encriptado: "  
    maquina.config(stackerbrett={" ":" ",".":"."},keyword="AAA")

def guardar(ventana):
    global mEncriptado, mensajeCargado
    nuevoArchivo="Mensaje.txt"
    i = 1
    flag = True

    while(flag):
        if not path2.exists("Mensaje"+".txt"):
            flag = False

        elif not (path2.exists("Mensaje"+"("+str(i)+").txt")):
            flag = False
            nuevoArchivo = "Mensaje"+"("+str(i)+").txt"
        
        else:
            i += 1
    
    archv = open(nuevoArchivo, "a")
    archv.write(mEncriptado)
    archv.close()

    mensajeCargado['text'] = "Guardado en "+nuevoArchivo
    ventana.update()

def cargar(ventana):
    global txt_charge, mensajeCargado
    if(isinstance(txt_charge.get(), str)):
        lines = open(txt_charge.get(),"r")
        for line in lines:
            mensajeCargado['text'] = line
    else:
        mensajeCargado['text'] = "No se ha encontrado el .txt"
    ventana.update()
        

def ventana_iniciar(ventana):
    global listaLabels,listaBotones,rotor1,rotor2,rotor3,palabraEncriptada,palabraDesencriptada, txt_charge, mensajeCargado
    frme_venta_iniciar=Frame(ventana,width=750,height=695,bg="#FFE4B5")
    frme_venta_iniciar.place(x=0,y=0)
    frm_secundario=Frame(ventana,width=400,height=200,bg="#FFE4B5")
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
    btn_reiniciar=Button(ventana,text="Reiniciar",command=lambda:[reiniciar()],highlightthickness=1,bd=3,activebackground="khaki1")
    btn_reiniciar.place(x=20,y=640)
    btn_guardar=Button(ventana,text="Guardar Mensaje",command=lambda:[guardar(ventana)],highlightthickness=1,bd=3,activebackground="khaki1")
    btn_guardar.place(x=100,y=640)
    btn_cargar=Button(ventana,text="Cargar Mensaje",command=lambda:[cargar(ventana)],highlightthickness=1,bd=3,activebackground="khaki1")
    btn_cargar.place(x=220,y=640)
    txt_charge=ttk.Entry(width = 20)
    txt_charge.place(x=340,y=645)
    txt_charge.insert(0, "Mensaje.txt")
    mensajeCargado=Label(ventana,text="",bd=10,bg="#FFE4B5")
    mensajeCargado.place(x=470,y=635)
    valores=[]
    for x in range(len(teclado)):
        for y in range(len(teclado[0])):
            valores+=[teclado[x][y]]
    valores.sort()
    valores.remove("Ñ")
    combo1 = ttk.Combobox(
        state="readonly",
        values=valores,
        width=8
    )
    combo1.place(x=150,y=600)
    combo2 = ttk.Combobox(
        state="readonly",
        values=valores,
        width=8
    )
    combo2.place(x=250,y=600)
    combo3 = ttk.Combobox(
        state="readonly",
        values=valores,
        width=8
    )
    combo3.place(x=350,y=600)
    btn_cambiar_Keyword=Button(ventana,text="Nueva Keyword",command=lambda:[cambiarKeyword([combo3.get(),combo2.get(),combo1.get()])],highlightthickness=1,bd=3,activebackground="khaki1")
    btn_cambiar_Keyword.place(x=430,y=600)
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
