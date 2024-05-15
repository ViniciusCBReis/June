import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import Train.Validador as val

def update_pie_chart(var1, var2, var3):
    # Função para atualizar o gráfico circular com as variáveis fornecidas
    sizes = [var1, var2, var3]
    labels = ['Positivo', 'Irrelevante', 'Negativo']
    plt.clf()  # Limpa o gráfico anterior
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', wedgeprops=dict(width=0.3))
    plt.gca().add_artist(plt.Circle((0,0),0.2,color='white', fc='white',linewidth=1.25))
    plt.axis('equal')  # Mantém o gráfico circular
    plt.draw()  # Desenha o gráfico atualizado

def update_text(new_text):
    # Função para atualizar o texto
    text_label.config(text=new_text)

def button1_clicked():
    # Função a ser executada quando o primeiro botão for clicado
    print("Botão 1 clicado")
    texto = text_entry.get("1.0", tk.END).strip()
    update_text(val.classificar_mensagem(texto))

def button2_clicked():
    # Função a ser executada quando o segundo botão for clicado
    print("Botão 2 clicado")
    texto = text_entry.get("1.0", tk.END).strip()
    var1, var2, var3 = val.avaliarmulti(texto)
    update_pie_chart(var1,var2,var3)

# Função principal para criar a interface
def main():
    global text_entry, text_label  # Define os campos de entrada e rótulo como variáveis globais
    # Criando a janela principal
    root = tk.Tk()
    root.geometry("1200x650")  # Definindo o tamanho da janela
    root.title("June")
    root.configure(bg="#2b2b2b")  # Configurando cor de fundo para o tema noturno
    root.resizable(False, False)  # Desabilita a capacidade de redimensionamento da janela

    # Criando um estilo para os campos de entrada com cantos arredondados
    style = ttk.Style()
    style.theme_use('clam')  # Mudando para um tema que suporta a estilização dos Entry
    style.configure('Rounded.TEntry', borderwidth=0, relief="flat", background="#464646", 
                    fieldbackground="#464646", bordercolor="#464646", foreground="white", 
                    font=('Helvetica', 10))

    # Criando um estilo personalizado com fundo mais escuro
    style = ttk.Style()

    # Configurando as cores do estilo
    style.configure("Custom.TFrame", background="#1f1f1f", foreground="white")  # Cores personalizadas para o fundo e texto

    # Criando um quadro usando o estilo personalizado
    frame = ttk.Frame(root, style="Custom.TFrame")
    frame.pack(padx=20, pady=20, fill='both', expand=True)

    # Criando um campo de texto
    text_entry = tk.Text(frame, width=60, height=10, bg="#464646", fg="white", 
                         font=('Helvetica', 10))
    text_entry.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Criando os botões
    button1 = ttk.Button(frame, text="Avaliar", command=button1_clicked)
    button1.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

    button2 = ttk.Button(frame, text="Avaliar Vários", command=button2_clicked)
    button2.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    # Criando um rótulo para o texto abaixo dos botões
    text_label = ttk.Label(frame, text=" ", background="#464646", 
                           foreground="white", font=('Helvetica', 24))
    text_label.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

   # Configurando o gráfico circular inicialmente
    fig, ax = plt.subplots()
    sizes = np.random.rand(3)
    labels = ['Positivo', 'Negativo', 'Irrelevante']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', wedgeprops=dict(width=0.3))
    ax.add_artist(plt.Circle((0,0),0.2,color='white', fc='white',linewidth=1.25))
    ax.axis('equal')  # Mantém o gráfico circular

    # Integrando o gráfico ao Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)

    # Expandindo as células vazias para preencher o espaço
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Iniciando o loop de eventos da interface gráfica
    root.mainloop()


if __name__ == "__main__":
    main()