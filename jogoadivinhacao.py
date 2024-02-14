import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")
        self.root.geometry("300x150")

        self.numero_aleatorio = random.randint(1, 100)
        self.tentativas = 0

        self.label_instrucao = tk.Label(root, text="Tente adivinhar o número (1-100):")
        self.label_instrucao.pack(pady=10)

        self.entry_palpite = tk.Entry(root)
        self.entry_palpite.pack(pady=10)

        self.botao_adivinhar = tk.Button(root, text="Adivinhar", command=self.verificar_palpite)
        self.botao_adivinhar.pack()

    def verificar_palpite(self):
        palpite = self.entry_palpite.get()

        try:
            palpite = int(palpite)
            self.tentativas += 1

            if palpite == self.numero_aleatorio:
                messagebox.showinfo("Parabéns!", f"Você adivinhou o número em {self.tentativas} tentativas.")
                self.root.destroy()
            elif palpite < self.numero_aleatorio:
                messagebox.showinfo("Tente novamente", "Tente um número maior.")
            else:
                messagebox.showinfo("Tente novamente", "Tente um número menor.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
