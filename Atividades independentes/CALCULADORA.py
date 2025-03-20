import tkinter as tk
from tkinter import messagebox

# Definindo a quantidade de horas por dia-------------------------------------------------------------------------------------
HORAS_POR_DIA = 4

def calcular_faltas():
    try:
        carga_horaria_horas = float(entry_carga_horaria.get())
        faltas_dias = float(entry_faltas.get())
        
        if carga_horaria_horas <= 0:
            messagebox.showerror("Erro", "A carga horária deve ser maior que zero.")
            return
        
        # Convertendo carga horária de horas para dias
        carga_horaria_dias = carga_horaria_horas / HORAS_POR_DIA
        
        # Cálculo da porcentagem de faltas
        porcentagem_faltas = (faltas_dias / carga_horaria_dias) * 100
        
        # Cálculo do limite de faltas permitidas (25% da carga horária)
        limite_faltas = carga_horaria_dias * 0.25
        
        resultado = f"Você teve {porcentagem_faltas:.2f}% de faltas."
        
        if faltas_dias > limite_faltas:
            resultado += "\nVocê foi reprovado por faltas."
        else:
            dias_restantes = limite_faltas - faltas_dias
            resultado += f"\nVocê pode faltar até {dias_restantes:.2f} dias sem ser reprovado."

        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela principal -----------------------------------------------------------------------------------------------------
janela = tk.Tk();
janela.title("Calculadora de Faltas");
janela.geometry("400x350");
janela.configure(bg="#f0f0f0");

# Criando os widgets
label_titulo = tk.Label(janela, text="Calculadora de Faltas", font=("Arial", 16, "bold"), bg="#f0f0f0");
label_titulo.pack(pady=10);

label_carga_horaria = tk.Label(janela, text="Carga Horária da Matéria (em horas):", bg="#f0f0f0");
label_carga_horaria.pack(pady=5);

entry_carga_horaria = tk.Entry(janela, font=("Arial", 12));
entry_carga_horaria.pack(pady=5);

label_faltas = tk.Label(janela, text="Faltas em Dias:", bg="#f0f0f0");
label_faltas.pack(pady=5);

entry_faltas = tk.Entry(janela, font=("Arial", 12));
entry_faltas.pack(pady=5);

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_faltas, font=("Arial", 12), bg="#4CAF50", fg="white");
botao_calcular.pack(pady=15);

label_resultado = tk.Label(janela, text="", font=("Arial", 12), bg="#f0f0f0");
label_resultado.pack(pady=10);

# Iniciando o loop da interface-----------------------------------------------------------------------------------------------------
janela.mainloop()