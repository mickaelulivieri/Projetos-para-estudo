from tkinter import *
from datetime import datetime

#Comandos para definir a estrutura/formato da aplicação

janela=Tk()
janela.title("Relógio Digital")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE) #Impossibilita mudar o tamanho
janela.configure(bg='#3d3d3d')

# python relogio.py para testar a aplicação

def relogio():
    tempo= datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana= tempo.strftime("%A")
    dia = tempo.day
    mes= tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text= hora)

    l1.after(200, relogio) # para atualizar

    l2.config(text= dia_semana + "  " +str(dia) + "/" + str(mes) + "/" + str(ano))

#para hora e dia da semana

l1= Label(janela, text ="",font=("Arial 80"), bg="black", fg="blue")
l1.grid(row=0, column=0, sticky=NW, padx=5)


l2= Label(janela, text ="",font=("Arial 20"), bg="black", fg="blue")
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()