import tkinter as tk
from tkinter import messagebox

class TaskApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación de Tareas")
        
        self.tasks = []
        
        self.label_desc = tk.Label(master, text="Descripción:")
        self.label_desc.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.entry_desc = tk.Entry(master, width=30)
        self.entry_desc.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_category = tk.Label(master, text="Categoría:")
        self.label_category.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        self.category_var = tk.StringVar(master)
        self.category_var.set("trabajo")  # Valor por defecto
        self.category_options = ["trabajo", "personal", "iglesia"]
        self.entry_category = tk.OptionMenu(master, self.category_var, *self.category_options)
        self.entry_category.grid(row=1, column=1, padx=5, pady=5)
        
        self.label_priority = tk.Label(master, text="Prioridad:")
        self.label_priority.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        self.priority_var = tk.IntVar(master)
        self.priority_var.set(1)  # Valor por defecto
        self.priority_options = [1, 2, 3]
        self.entry_priority = tk.OptionMenu(master, self.priority_var, *self.priority_options)
        self.entry_priority.grid(row=2, column=1, padx=5, pady=5)
        
        self.btn_add_task = tk.Button(master, text="Agregar Tarea", command=self.add_task)
        self.btn_add_task.grid(row=3, columnspan=2, padx=5, pady=5)
        
        self.listbox_tasks = tk.Listbox(master, width=50)
        self.listbox_tasks.grid(row=4, columnspan=2, padx=5, pady=5)
        
    def add_task(self):
        desc = self.entry_desc.get()
        category = self.category_var.get()
        priority = self.priority_var.get()
        
        if desc:
            self.tasks.append({"Descripción": desc, "Categoría": category, "Prioridad": priority})
            self.update_task_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Por favor, complete la descripción de la tarea.")
            
    def update_task_listbox(self):
        self.listbox_tasks.delete(0, tk.END)
        for task in self.tasks:
            self.listbox_tasks.insert(tk.END, f"{task['Descripción']} - {task['Categoría']} - {task['Prioridad']}")
            
    def clear_entries(self):
        self.entry_desc.delete(0, tk.END)
        self.category_var.set("trabajo")  # Reiniciar a valor por defecto
        self.priority_var.set(1)  # Reiniciar a valor por defecto
        
def main():
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
