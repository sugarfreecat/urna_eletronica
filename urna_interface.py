import tkinter as tk
from tkinter import messagebox
from urna_poo import UrnaEletronica

class InterfaceGrafica:
    def __init__(self, urna):
        self.urna = urna
        self.janela = tk.Tk()
        self.janela.title("Urna Eletrônica")
        self.iniciar_interface()

    def iniciar_interface(self):
        """Inicia a interface gráfica da urna eletrônica."""
        # Entrada de título
        tk.Label(self.janela, text="Título do Eleitor:").grid(row=0, column=0, padx=10, pady=10)
        self.entrada_titulo = tk.Entry(self.janela)
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=10)

        # Botão para verificar eleitor
        tk.Button(self.janela, text="Verificar", command=self.verificar_eleitor).grid(row=0, column=2, padx=10, pady=10)

        # Nome do eleitor
        self.eleitor_nome = tk.StringVar()
        tk.Label(self.janela, text="Eleitor:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.janela, textvariable=self.eleitor_nome).grid(row=1, column=1, padx=10, pady=10)

        # RG do eleitor
        self.eleitor_rg = tk.StringVar()
        tk.Label(self.janela, text="RG:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.janela, textvariable=self.eleitor_rg).grid(row=2, column=1, padx=10, pady=10)

        # CPF do eleitor
        self.eleitor_cpf = tk.StringVar()
        tk.Label(self.janela, text="CPF:").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.janela, textvariable=self.eleitor_cpf).grid(row=3, column=1, padx=10, pady=10)

        # Entrada de número do candidato
        tk.Label(self.janela, text="Número do Candidato:").grid(row=4, column=0, padx=10, pady=10)
        self.entrada_numero = tk.Entry(self.janela)
        self.entrada_numero.grid(row=4, column=1, padx=10, pady=10)

        # Botões para votar
        tk.Button(self.janela, text="Votar", command=self.votar).grid(row=5, column=0, columnspan=3, pady=10)

        self.janela.mainloop()

    def verificar_eleitor(self):
        # Verifica o eleitor pelo título
        titulo = self.entrada_titulo.get()
        eleitor = self.urna.verificar_eleitor(titulo)
        if eleitor:
            self.eleitor_nome.set(f"Nome: {eleitor.nome}")
            self.eleitor_rg.set(f"RG: {eleitor.rg}")
            self.eleitor_cpf.set(f"CPF: {eleitor.cpf}")
        else:
            messagebox.showerror("Erro", "Eleitor não encontrado.")
            self.eleitor_nome.set("")
            self.eleitor_rg.set("")
            self.eleitor_cpf.set("")

    def votar(self):
        # Registra o voto de um eleitor
        numero = self.entrada_numero.get()
        if numero:
            candidato = self.urna.verificar_candidato(numero)
            if candidato:
                self.urna.registrar_voto(numero)
                messagebox.showinfo("Voto Computado", f"Voto registrado para {candidato.nome}!")
            else:
                self.urna.registrar_voto("Inválido")
                messagebox.showinfo("Voto Computado", "Voto registrado como Inválido!")
        else:
            self.urna.registrar_voto("Branco")
            messagebox.showinfo("Voto Computado", "Voto registrado como Branco!")

        # Limpa campos para o próximo eleitor
        self.eleitor_nome.set("")
        self.eleitor_rg.set("")
        self.eleitor_cpf.set("")
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_numero.delete(0, tk.END)

# Cria a urna eletrônica e a interface gráfica
if __name__ == "__main__":
    urna = UrnaEletronica()
    InterfaceGrafica(urna)