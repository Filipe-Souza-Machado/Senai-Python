#IMPORTS---------------------------------------------------------------------
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

#FUNÇÕES---------------------------------------------------------------------
def add_tarefa():
    t = tarefa.get();
    
    if (t):
        lista_tarefas.insert(0,t);
        tarefa.delete(0,'end');
    else:
        messagebox.showerror('Error ' ,' O campo tarefa esta vazio!!');

def del_tarefa():
    selecionada = lista_tarefas.curselection();
    
    if (selecionada):
        lista_tarefas.delete(selecionada);
    else:
        messagebox.showerror('Error ' ,' Nenhuma tarefa foi selecionada!!'); 

#----------------------------------------------------------------------------

#Janela----------------------------------------------------------------------
janela = ctk.CTk();
ctk.set_appearance_mode("dark");
janela.title("Lista de tarefas - 1.0");
janela.geometry("350x500");
janela.resizable(False,False);
#----------------------------------------------------------------------------

#INPUT-----------------------------------------------------------------------
tarefa = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='hotpink',
                      placeholder_text='Digite a tarefa a ser criada',
                      );
tarefa.pack(pady=10);
#----------------------------------------------------------------------------

#BUTõES----------------------------------------------------------------------
btnAdicionar = ctk.CTkButton(janela,
                             width=100,
                             height=40,
                             fg_color='lightgreen',
                             hover_color='darkgreen',
                             text='➕Adicionar tarefa',
                             font=('verdana',15,'bold'),
                             cursor='hand2',
                             text_color='black',
                             command=add_tarefa
                             );
btnAdicionar.place(x=20,y=80);

btnDeletar = ctk.CTkButton(janela,
                             width=100,
                             height=40,
                             fg_color='red',
                             hover_color='darkred',
                             text='Deletar tarefa',
                             font=('verdana',15,'bold'),
                             cursor='hand2',
                             text_color='white',
                             command=del_tarefa
                             );
btnDeletar.place(x=205,y=80);
#------------------------------------------------------------------------------

#LISTA-------------------------------------------------------------------------
lista_tarefas = Listbox(janela,
                        width=28,
                        height=17,
                        font=('verdana',12,'bold'),
                        fg='white',
                        background='#323232',
                        highlightbackground='hotpink',
                        highlightthickness=2,                        
                        );
lista_tarefas.place(x=21, y=150);
#-------------------------------------------------------------------------------
janela.mainloop();