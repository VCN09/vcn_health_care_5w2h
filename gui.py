import tkinter as tk
from tkinter import messagebox
from task import Tarefa
from database import Database

class Matriz5W2H:
    def __init__(self, root):
        self.db = Database('localhost', 'root', 'password', 'vcn_health_care')
        self.root = root
        self.root.title("VCN Health Care - Matriz 5W2H")

        self.background = tk.PhotoImage(file="background.png")
        self.background_label = tk.Label(root, image=self.background)
        self.background_label.place(relwidth=1, relheight=1)

        # Labels e Entradas
        self.labels = ["What", "Why", "Wher", "Whe", "Who", "How", "How Much", "priority", "Statu"]
        self.entries = {}

        for i, label in enumerate(self.labels):
            tk.Label(root, text=label, bg="#ADD8E6").grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(root, width=50)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry

        # Botão para Adicionar Tarefa
        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=len(self.labels), column=0, columnspan=2, pady=10)

        # Lista de Tarefas
        self.task_list = tk.Listbox(root, width=100, height=10)
        self.task_list.grid(row=len(self.labels) + 1, column=0, columnspan=2, padx=10, pady=10)
        self.load_tasks()

    def add_task(self):
        task = Tarefa(
            self.entries["What"].get(),
            self.entries["Why"].get(),
            self.entries["Wher"].get(),
            self.entries["Whe"].get(),
            self.entries["Who"].get(),
            self.entries["How"].get(),
            self.entries["How Much"].get(),
            self.entries["priority"].get(),
            self.entries["Statu"].get()
        )

        if all([getattr(task, field) for field in self.labels]):
            self.db.insert_task(task)
            self.task_list.insert(tk.END, str(task))
            for entry in self.entries.values():
                entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def load_tasks(self):
        tasks = self.db.fetch_tasks()
        for task in tasks:
            task_str = " | ".join(f"{self.labels[i]}: {task[i+1]}" for i in range(len(self.labels)))
            self.task_list.insert(tk.END, task_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = Matriz5W2H(root)
    root.mainloop()
